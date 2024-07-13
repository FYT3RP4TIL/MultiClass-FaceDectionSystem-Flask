from flask import Flask, render_template, request, redirect, url_for, flash, session
import os
from DataProcessing import preprocess_images
import tempfile
import shutil

app = Flask(__name__)
app.secret_key = 'upersecretkey'

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/navigation')
def navigation():
    return render_template('navigation.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'admin' and password == 'admin':
            return redirect(url_for('navigation'))
        else:
            flash('Invalid credentials, please try again.', 'error')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    flash('You have been logged out.', 'Success')
    return redirect(url_for('login'))

@app.route('/upload')
def train_facial_reco():
    return render_template('upload_image_for_clean_training.html')

@app.route('/train_m')
def train_model_under():
    return render_template('training_under_process.html')

@app.route('/upload_image', methods=['POST'])
def upload_image():
    folder_name = request.form['folderName']
    images = request.files.getlist('image')  # Get multiple files

    if not folder_name:
        flash('Folder name is missing.', 'error')
        return redirect(url_for('train_facial_reco'))
    
    if not images:
        flash('No images selected for upload.', 'error')
        return redirect(url_for('train_facial_reco'))

    folder_path = os.path.join(app.config['UPLOAD_FOLDER'], 'Data', folder_name)

    if os.path.exists(folder_path):
        temp_dir = tempfile.mkdtemp()  # Create a temporary directory to store the images
        for image in images:
            image_path = os.path.join(temp_dir, image.filename)
            image.save(image_path)

        # Store folder_name and temp_dir in session
        session['folder_name'] = folder_name
        session['temp_dir'] = temp_dir

        flash('Folder already exists!', 'error')
        return redirect(url_for('popup_page'))
    
    os.makedirs(folder_path, exist_ok=True)

    if images:
        for image in images:
            image_path = os.path.join(folder_path, image.filename)
            image.save(image_path)

        # Preprocess the uploaded images
        output_folder = os.path.join(app.config['UPLOAD_FOLDER'], 'Cropped_Data', folder_name)
        preprocess_images(folder_path, output_folder)

        flash('Images uploaded and processed successfully!', 'success')
        return redirect(url_for('up_confirm'))
    else:
        flash('Failed to upload images.', 'error')
        return redirect(url_for('train_facial_reco'))


@app.route('/add_photos', methods=['POST'])
def add_photos():
    folder_name = request.form['folderName']
    temp_dir = request.form['tempDir']

    if not folder_name or not temp_dir:
        flash('Missing folder name or temporary directory.', 'error')
        return redirect(url_for('train_facial_reco'))

    folder_path = os.path.join(app.config['UPLOAD_FOLDER'], 'Data', folder_name)

    try:
        # Move images from temp_dir to folder_path
        for file_name in os.listdir(temp_dir):
            temp_image_path = os.path.join(temp_dir, file_name)
            final_image_path = os.path.join(folder_path, file_name)
            shutil.move(temp_image_path, final_image_path)
        
        shutil.rmtree(temp_dir)  # Remove temporary directory

        # Preprocess the uploaded images
        output_folder = os.path.join(app.config['UPLOAD_FOLDER'], 'Cropped_Data', folder_name)
        preprocess_images(folder_path, output_folder)

        flash('New images uploaded and processed successfully!', 'success')
        return redirect(url_for('up_confirm'))
    
    except Exception as e:
        flash(f'Failed to upload images: {str(e)}', 'error')
        return redirect(url_for('train_facial_reco'))
    
@app.route('/discard', methods=['POST'])
def discard():
    flash('Upload discarded.', 'info')
    return redirect(url_for('train_facial_reco'))

@app.route('/face_detection')
def face_detection():
    return render_template('face_detection_page.html')

@app.route('/forgot_password')
def forgot_password():
    return "Forgot Password Page"

@app.route('/u_confirm')
def up_confirm():
    return render_template('upload_confirmation_page.html')

@app.route('/popup_page')
def popup_page():
    folder_name = session.get('folder_name')
    temp_dir = session.get('temp_dir')
    return render_template('popup_page.html', folder_name=folder_name, temp_dir=temp_dir)

if __name__ == '__main__':
    app.run(debug=True)