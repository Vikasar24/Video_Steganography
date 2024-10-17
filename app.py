from flask import Flask, render_template, request, send_from_directory, redirect, url_for
import os
from werkzeug.utils import secure_filename
from steganography import embed_message, extract_message

app = Flask(__name__)

# Configuration
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['OUTPUT_FOLDER'] = 'outputs'
app.config['ALLOWED_EXTENSIONS'] = {'mp4', 'avi', 'mov', 'mkv'}

# Ensure upload and output directories exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/embed', methods=['POST'])
def embed():
    if 'video' not in request.files:
        return redirect(request.url)
    
    file = request.files['video']
    message = request.form['message']
    
    if file.filename == '':
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(input_path)
        
        output_filename = f"stego_{filename.rsplit('.', 1)[0]}.avi"
        output_path = os.path.join(app.config['OUTPUT_FOLDER'], output_filename)
        
        embed_message(input_path, output_path, message)
        
        download_link = url_for('download_file', filename=output_filename)
        return render_template('index.html', download_link=download_link)
    
    return redirect(url_for('index'))

@app.route('/extract', methods=['POST'])
def extract():
    if 'stego_video' not in request.files:
        return redirect(request.url)
    
    file = request.files['stego_video']
    
    if file.filename == '':
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        stego_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(stego_path)
        
        message = extract_message(stego_path)
        return render_template('index.html', extracted_message=message)
    
    return redirect(url_for('index'))

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER'], filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
