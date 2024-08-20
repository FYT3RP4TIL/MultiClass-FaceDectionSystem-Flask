# MultiClass-FaceDectionSystem-Flask
![](https://github.com/user-attachments/assets/7c5fc8c3-6556-4b49-af19-cbb9b3193b6f)
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

# [Deepface](https://github.com/serengil/deepface)
<p align="center"><img src="https://github.com/user-attachments/assets/96014b9d-89c1-4eee-b8b7-f99e14f7e17c" width="95%" height="95%"></p>

**Face recognition models** 

DeepFace is a **hybrid** face recognition package. It currently wraps many **state-of-the-art** face recognition models: [`VGG-Face`](https://sefiks.com/2018/08/06/deep-face-recognition-with-keras/) , [`FaceNet`](https://sefiks.com/2018/09/03/face-recognition-with-facenet-in-keras/), [`OpenFace`](https://sefiks.com/2019/07/21/face-recognition-with-openface-in-keras/), [`DeepFace`](https://sefiks.com/2020/02/17/face-recognition-with-facebook-deepface-in-keras/), [`DeepID`](https://sefiks.com/2020/06/16/face-recognition-with-deepid-in-keras/), [`ArcFace`](https://sefiks.com/2020/12/14/deep-face-recognition-with-arcface-in-keras-and-python/), [`Dlib`](https://sefiks.com/2020/07/11/face-recognition-with-dlib-in-python/), `SFace` and `GhostFaceNet`. The default configuration uses VGG-Face model.

```python
models = [
  "VGG-Face", 
  "Facenet", 
  "Facenet512", 
  "OpenFace", 
  "DeepFace", 
  "DeepID", 
  "ArcFace", 
  "Dlib", 
  "SFace",
  "GhostFaceNet",
]

#face verification
result = DeepFace.verify(
  img1_path = "img1.jpg",
  img2_path = "img2.jpg",
  model_name = models[0],
)

#face recognition
dfs = DeepFace.find(
  img_path = "img1.jpg",
  db_path = "C:/workspace/my_db", 
  model_name = models[1],
)

#embeddings
embedding_objs = DeepFace.represent(
  img_path = "img.jpg",
  model_name = models[2],
)
```

FaceNet, VGG-Face, ArcFace and Dlib are overperforming ones based on experiments - see [`BENCHMARKS`](https://github.com/serengil/deepface/tree/master/benchmarks) for more details. You can find the measured scores of various models in DeepFace and the reported scores from their original studies in the following table.

| Model          | Measured Score | Declared Score     |
| -------------- | -------------- | ------------------ |
| Facenet512     | 98.4%          | 99.6%              |
| Human-beings   | 97.5%          | 97.5%              |
| Facenet        | 97.4%          | 99.2%              |
| Dlib           | 96.8%          | 99.3 %             |
| VGG-Face       | 96.7%          | 98.9%              |
| ArcFace        | 96.7%          | 99.5%              |
| GhostFaceNet   | 93.3%          | 99.7%              |
| SFace          | 93.0%          | 99.5%              |
| OpenFace       | 78.7%          | 92.9%              |
| DeepFace       | 69.0%          | 97.3%              |
| DeepID         | 66.5%          | 97.4%              |

Conducting experiments with those models within DeepFace may reveal disparities compared to the original studies, owing to the adoption of distinct detection or normalization techniques. Furthermore, some models have been released solely with their backbones, lacking pre-trained weights. Thus, we are utilizing their re-implementations instead of the original pre-trained weights.

For more information and on how to use the library go to library `https://github.com/serengil/deepface`
