from flask import Flask, request, render_template, send_file
import os
import glob
from PIL import Image
import numpy as np
import shutil
import zipfile
import time

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
PROCESSED_FOLDER = 'processed'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

def find_duplicate_images(directory, resolution=(100, 100)):
    image_files = glob.glob(os.path.join(directory, "*"))
    image_hashes = {}
    for image_file in image_files:
        try:
            with Image.open(image_file) as img:
                img = img.convert('RGB')
                img_resized = img.resize(resolution, Image.LANCZOS)
                img_array = np.array(img_resized)
                img_hash = hash(img_array.tobytes())
                if img_hash in image_hashes:
                    os.remove(image_file)
                else:
                    image_hashes[img_hash] = image_file
        except Exception as e:
            print(f"Error processing {image_file}: {e}")

def zip_directory(directory, zip_filename):
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for root, dirs, files in os.walk(directory):
            for file in files:
                zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), directory))

@app.route('/', methods=['GET', 'POST'])
def upload_folder():
    if request.method == 'POST':
        if 'folder' not in request.files:
            return 'No folder part'
        folder = request.files.getlist('folder')
        folder_name = os.path.join(UPLOAD_FOLDER, folder[0].filename.split('/')[0])
        os.makedirs(folder_name, exist_ok=True)
        for file in folder:
            file.save(os.path.join(folder_name, file.filename.split('/')[-1]))
        
        find_duplicate_images(folder_name)
        
        processed_folder_name = os.path.join(PROCESSED_FOLDER, os.path.basename(folder_name))
        if os.path.exists(processed_folder_name):
            shutil.rmtree(processed_folder_name)
        
        shutil.move(folder_name, processed_folder_name)
        
        zip_path = os.path.join(PROCESSED_FOLDER, os.path.basename(folder_name) + '.zip')
        zip_directory(processed_folder_name, zip_path)
        
        return send_file(zip_path, as_attachment=True)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
