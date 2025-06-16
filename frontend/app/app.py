import os
import sys
import requests
from werkzeug.utils import secure_filename
from flask import Flask, request, redirect, render_template, flash, url_for, jsonify
import threading
import subprocess
# from backend.app.move_files_to_archive import move_files_to_archive
# from backend.app.remove_empty_folders import remove_empty_folders

app = Flask(__name__)
app.secret_key = 'baxtersecretkey'
FASTAPI_URL = "http://rag_fastapi:8001"
#DOWNLOAD_TEMPLATE_FOLDER = 'shared_data/input_templates'

# Base upload folder
UPLOAD_FOLDER = 'shared_data/uploads/'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'pdf', 'docx', 'xlsx', 'xls', 'jpg', 'jpeg', 'png'}
app.config['ALLOWED_TEMPLATE_EXTENSIONS'] = {'xlsx', 'xls'}

# Base upload folder
UPLOAD_INPUT_TEMPLATE_FOLDER = 'shared_data/input_templates/'
os.makedirs(UPLOAD_INPUT_TEMPLATE_FOLDER, exist_ok=True)
app.config['UPLOAD_INPUT_TEMPLATE_FOLDER'] = UPLOAD_INPUT_TEMPLATE_FOLDER

DOWNLOAD_TEMPLATE_FOLDER = 'shared_data/output_templates/'
app.config['DOWNLOAD_TEMPLATE_FOLDER'] = DOWNLOAD_TEMPLATE_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def allowed_template_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_TEMPLATE_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def index():
    answer = ''
    if request.method == 'POST':
        question = request.form['question']
        r = requests.post(f"{FASTAPI_URL}/ask", json={"question": question})
        answer = r.json().get('answer', '')
    return render_template('index.html', answer=answer)

@app.route("/overview")
def overview():
    return render_template("overview.html")

@app.route('/reports')
def reports():
    input_files = os.listdir(UPLOAD_INPUT_TEMPLATE_FOLDER)
    output_files = os.listdir(DOWNLOAD_TEMPLATE_FOLDER)
    
    return render_template(
        "reports.html",
        input_files=input_files,
        output_files=output_files,
        fastapi_url="http://localhost:8001"
    )

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/chat', methods=['POST'])
def chat():
    payload = request.json
    user_query = payload.get("user_query", "").strip()
    if not user_query:
        return jsonify({"response": "Oops! Type something first, love!"}), 400
    
    response = requests.post(f"{FASTAPI_URL}/retrieval", json={"user_query": user_query})
    response_data = response.json()
    return jsonify(response_data)
    #return render_template('chatbot.html')

@app.route('/prompt_template')
def prompt_template():
    return render_template('prompt_template.html')

@app.route('/prompt', methods=['POST'])
def prompt():
    payload = request.json
    user_query = payload.get("user_query", "").strip()
    prompt_query = payload.get("prompt_query", "").strip()
    if not user_query:
        return jsonify({"response": "Oops! Type something first, love!"}), 400
    response = requests.post(f"{FASTAPI_URL}/prompt", json={"prompt_query": prompt_query, "user_query": user_query})
    response_data = response.json()
    return jsonify(response_data)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        #handle_template_file_upload_response = handle_template_file_upload()
        return handle_file_upload()
    return render_template('upload.html')

@app.route('/upload_input_template', methods=['GET', 'POST'])
def upload_input_template():
    if request.method == 'POST':
         return handle_template_file_upload()
    return render_template('upload_input_template.html')

def handle_template_file_upload():
    template_files = request.files.getlist('files')
    if not template_files or template_files[0].filename == '':
        flash("No template file(s) selected.")
        return redirect(request.url)

    for file in template_files:
        if file and allowed_template_file(file.filename):
            # Maintain folder structure from the uploaded filename
            filename = file.filename.replace("..", "").strip("/")  # Sanitize
            full_path = os.path.join(app.config['UPLOAD_INPUT_TEMPLATE_FOLDER'], filename)
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            file.save(full_path)

    return jsonify({"status": "success", "message": f"Uploaded {len(template_files)} template file(s) successfully."})


def handle_file_upload():
    files = request.files.getlist('files')
       
    if not files or files[0].filename == '':
        flash("No files selected.")
        return redirect(request.url)

    for file in files:
        if file and allowed_file(file.filename):
            # Maintain folder structure from the uploaded filename
            filename = file.filename.replace("..", "").strip("/")  # Sanitize
            full_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            file.save(full_path)

    flash(f"Uploaded {len(files)} file(s) successfully.")

    # move files to destination folder
    try:
        response = requests.post(f"{FASTAPI_URL}/vectorization", json={"folder_path": UPLOAD_FOLDER})
        response.raise_for_status()
        response_data = response.json()
        api_message = response_data.get('message', '')
        api_status = response_data.get('status', '')
        message = f"Uploaded {len(files)} file(s) and \n\n{api_message}"
        # Build combined response
        final_response = {
            'status': api_status,
            'message': message
        }
    except ValueError:
        return jsonify({'error': 'Invalid JSON response from vectorization API'}), 500

    return jsonify(final_response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
