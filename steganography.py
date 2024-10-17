import cv2
import numpy as np

def embed_message(video_path, output_path, message):
    # Convert message to binary
    binary_message = ''.join([format(ord(char), '08b') for char in message]) + '1111111111111110'  # Delimiter
    
    cap = cv2.VideoCapture(video_path)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, cap.get(cv2.CAP_PROP_FPS),
                          (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                           int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))
    
    frame_count = 0
    bit_index = 0
    total_bits = len(binary_message)
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        if bit_index < total_bits:
            # Embed bits into the frame
            for row in range(frame.shape[0]):
                for col in range(frame.shape[1]):
                    for channel in range(frame.shape[2]):
                        if bit_index < total_bits:
                            # Modify the LSB of the pixel
                            frame[row, col, channel] = (frame[row, col, channel] & ~1) | int(binary_message[bit_index])
                            bit_index += 1
                        else:
                            break
        out.write(frame)
        frame_count += 1
    
    cap.release()
    out.release()
    print(f"Message embedded in {output_path}")

def extract_message(video_path):
    cap = cv2.VideoCapture(video_path)
    binary_message = ""
    delimiter = '1111111111111110'
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        for row in range(frame.shape[0]):
            for col in range(frame.shape[1]):
                for channel in range(frame.shape[2]):
                    # Extract the LSB
                    binary_message += str(frame[row, col, channel] & 1)
                    if binary_message.endswith(delimiter):
                        cap.release()
                        # Convert binary to string
                        binary_message = binary_message[:-len(delimiter)]
                        message = ''.join([chr(int(binary_message[i:i+8], 2)) 
                                           for i in range(0, len(binary_message), 8)])
                        return message
    cap.release()
    return "No hidden message found."
