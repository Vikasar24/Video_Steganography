
# Video Steganography Web Application

This project is a web-based application that allows users to hide and retrieve secret messages within video files using **steganography**. The project is built using **Python (Flask)** for the backend, **OpenCV** for handling video processing, and **HTML/CSS** for the frontend. The hidden message is embedded into the least significant bits of the video frames, allowing it to be concealed within the video without altering the visual quality.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Deploying to a Server](#deploying-to-a-server)

---

## Features

- **Embed Message**: Hide secret messages inside a video file.
- **Extract Message**: Retrieve hidden messages from a video file.
- **User Interface**: A simple and clean interface built with HTML and CSS.
- **File Upload**: Upload video files in formats like `.mp4`, `.avi`, `.mov`, `.mkv`.
- **Download**: Download the stego video after the message has been embedded.

## Requirements

Before running the project, ensure you have the following dependencies installed:

- **Python 3.x**
- **Flask**: A lightweight web framework for Python.
- **OpenCV**: For handling video processing.
- **NumPy**: Required by OpenCV.
- **Werkzeug**: For handling file uploads.

## Installation

1. **Clone the Repository**:

   \`\`\`bash
   git clone https://github.com/your-username/video-steganography.git
   cd video-steganography
   \`\`\`

2. **Set Up a Virtual Environment (Optional but recommended)**:

   \`\`\`bash
   python -m venv venv
   source venv/bin/activate   # On macOS/Linux
   .\venv\Scripts\activate    # On Windows
   \`\`\`

3. **Install the Required Libraries**:

   \`\`\`bash
   pip install flask opencv-python numpy
   \`\`\`

4. **Run the Application**:

   \`\`\`bash
   python app.py
   \`\`\`

5. Open your web browser and visit: `http://127.0.0.1:5000`

## Usage

### Embedding a Message

1. On the homepage, upload a video file in one of the supported formats (`.mp4`, `.avi`, `.mov`, `.mkv`).
2. Enter the secret message you want to hide.
3. Click **Embed Message**. Once completed, you can download the stego video with the hidden message.

### Extracting a Message

1. On the homepage, upload a video file that contains a hidden message.
2. Click **Extract Message**. If a message is embedded, it will be displayed on the screen.

## Project Structure

The project's file structure is organized as follows:

\`\`\`
video_steganography/
├── app.py                 # Main Flask application
├── steganography.py        # Core steganography logic
├── templates/
│   └── index.html          # Frontend HTML template
├── static/
│   └── styles.css          # Frontend CSS styles
├── uploads/                # Directory to store uploaded videos
├── outputs/                # Directory to store processed stego videos
├── venv/                   # Virtual environment (if used)
└── README.md               # This README file
\`\`\`

### Key Files:

- **app.py**: The Flask backend which manages the server and handles routes for embedding/extracting messages.
- **steganography.py**: Contains the core logic for embedding and extracting messages using OpenCV.
- **index.html**: The main HTML template used for the web interface.
- **styles.css**: CSS file for styling the user interface.

## How It Works

### Embedding a Message

1. The user uploads a video and enters a secret message.
2. The message is converted into a binary format.
3. Using **Least Significant Bit (LSB) steganography**, the binary data is hidden in the video frames. The pixel values are slightly altered to encode the message.
4. The processed video with the hidden message is saved and available for download.

### Extracting a Message

1. The user uploads a video with a hidden message.
2. The LSBs of the pixel values in the video frames are read.
3. The binary data is converted back into the original message.
4. The extracted message is displayed to the user.

## Deploying to a Server

You can deploy this Flask application on various hosting platforms like **Heroku**, **PythonAnywhere**, or a **VPS**. Here's how you can deploy it to **Heroku**:

### Deploying to Heroku

1. **Install Heroku CLI**:
   If you haven't already installed the Heroku CLI, follow the instructions [here](https://devcenter.heroku.com/articles/heroku-cli).

2. **Create a `requirements.txt` file**:
   Run the following command to create a `requirements.txt` file which lists the dependencies needed by Heroku:

   \`\`\`bash
   pip freeze > requirements.txt
   \`\`\`

3. **Create a `Procfile`**:
   A `Procfile` tells Heroku how to run the application. In your project root, create a `Procfile` with the following content:

   \`\`\`
   web: python app.py
   \`\`\`

4. **Log in to Heroku**:

   \`\`\`bash
   heroku login
   \`\`\`

5. **Create a Heroku Application**:

   \`\`\`bash
   heroku create your-app-name
   \`\`\`

6. **Deploy to Heroku**:

   \`\`\`bash
   git add .
   git commit -m "Deploy video steganography app"
   git push heroku master
   \`\`\`

7. **Open the App**:

   \`\`\`bash
   heroku open
   \`\`\`

### Deploying on PythonAnywhere

1. Create an account on [PythonAnywhere](https://www.pythonanywhere.com/).
2. Upload the project files via the file manager.
3. Set up a **Flask Web App** via the "Web" tab on PythonAnywhere.
4. Configure the app to use **Flask** and the `app.py` file as the entry point.

For more information on deploying Flask apps, refer to the official documentation:
- [Heroku Flask Deployment](https://devcenter.heroku.com/articles/getting-started-with-python)
- [PythonAnywhere Flask Deployment](https://help.pythonanywhere.com/pages/Flask/)

---

## License

This project is licensed under the MIT License. Feel free to modify and use it as needed.
