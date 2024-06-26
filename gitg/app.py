from flask import Flask, render_template, request, redirect, url_for, send_from_directory, jsonify
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'pdf' not in request.files:
            return 'No file part'
        file = request.files['pdf']
        if file.filename == '':
            return 'No selected file'
        if file:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            return redirect(url_for('list_files'))
    return render_template('upload.html')

@app.route('/list')
def list_files():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    pdf_files = [f for f in files if f.endswith('.pdf')]
    return render_template('list.html', files=pdf_files)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/api/files')
def api_files():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    pdf_files = [f for f in files if f.endswith('.pdf')]
    return jsonify(pdf_files)

if __name__ == '__main__':
    app.run(port=5500, debug=True)
