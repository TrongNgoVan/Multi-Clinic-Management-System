from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'static/upload'
PUBLIC_PREFIX = '/static/upload/'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload_image', methods=['POST'])
def upload_image():
    if 'upload' not in request.files:
        return jsonify({'uploaded': 0, 'error': {'message': 'No file received'}})

    file = request.files['upload']

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        file.save(file_path)

        return jsonify({
            'uploaded': 1,
            'file': filename,
            'url': f'{PUBLIC_PREFIX}{filename}'
        })
    else:
        return jsonify({
            'uploaded': 0,
            'error': {'message': 'Invalid file extension'}
        })

if __name__ == '__main__':
    app.run(debug=True)
