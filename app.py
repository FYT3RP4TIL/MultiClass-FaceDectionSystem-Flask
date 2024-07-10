from flask import Flask, render_template, request, redirect, url_for, flash
import os

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
            flash('Login successful!', 'uccess')
            return redirect(url_for('navigation'))
        else:
            flash('Invalid credentials, please try again.', 'error')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    flash('You have been logged out.', 'uccess')
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
    image = request.files['image']

    folder_path = os.path.join(app.config['UPLOAD_FOLDER'], 'Data', folder_name)
    os.makedirs(folder_path, exist_ok=True)

    if image:
        image_path = os.path.join(folder_path, image.filename)
        image.save(image_path)
        flash('Image uploaded successfully!', 'uccess')
        return redirect(url_for('up_confirm'))
    else:
        flash('Failed to upload image.', 'error')
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


if __name__ == '__main__':
    app.run(debug=True)