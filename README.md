# MultiClass-FaceDectionSystem-Flask

## :bulb: Objective :

Develop a face recognition system that can take user input images and live video, preprocess them, store them, and recognize faces using DeepFace and the VGG16 model, displaying results through a web interface and is to develop a robust and user-friendly face recognition system that leverages advanced deep learning techniques to enhance security and personalization in various applications.

## Project Outline :

1. **Image Recognition with Haarcascade and OpenCV**
2. **Image Data Preprocessing**
3. **Face Recognition Classification Model with VGG16**
4. **Flask (HTML, CSS, HTTP Methods)**

Finally, we will integrate all these components to build a fully functional face recognition web app.

## 🚀&nbsp;Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/FYT3RP4TIL/MultiClass-FaceDectionSystem-Flask.git
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

- On Windows:
```bash
venv\Scripts\activate
```
- On macOS and Linux:
```bash
source venv/bin/activate
```
### 4. Install Dependencies
```bash
pip install -r requirements.txt
```
Restart venv to avoid any issues.
### 5. Run the App
```bash
python main.py
```
Open your web browser and go to http://127.0.0.1:5000/ to see the app in action.

# :cyclone: System Design

## Modules

### 1. User Interface (UI) Module
- **Description**: 
  - Develop HTML/CSS-based web pages for user interaction.
  - Implement forms for uploading images and accessing the live video feed.

### 2. Image/Video Capture Module
- **Description**: 
  - Capture images or live video from the user's device.
  - Provide functionality for users to upload images manually.

### 3. Preprocessing Module
- **Description**: 
  - Convert images to grayscale, resize, and normalize.
  - Detect and align faces within the images/video frames using OpenCV or similar libraries.

### 4. Face Recognition Module
- **Description**: 
  - Use DeepFace and VGG16 for feature extraction and face recognition.
  - Implement logic to compare input images with stored images for recognition.

### 5. Database Module
- **Description**: 
  - Store preprocessed images, extracted features in respected upload and predict folders

### 6. Results Display Module
- **Description**: 
  - Display recognized faces along with user details on the web interface.
  - Show real-time recognition results on the live video feed.

## System Flow ([Figma](https://www.figma.com/design/PYza59lyc3BrfsGVIkuRkx/MultiClass-Face-Detection-System-(View)?m=auto&t=iAkc1cWma8sntGfT-1))
1. **User Access**:
   - Users can upload images or initiate live video capture through the web interface.
  
2. **Preprocessing**:
   - Uploaded images or video frames are preprocessed to ensure consistency in face detection and recognition.

3. **Face Recognition**:
   - The preprocessed images are passed through the face recognition module, where features are extracted and compared against stored data.

4. **Results Storage**:
   - Recognition results, along with preprocessed images and metadata, are stored in dediacted folders.

5. **Results Display**:
   - The results of the recognition process are displayed on the web interface, updating in real-time for live video feeds.
