# Plant Disease Detection Backend

This project is a Flask-based backend for an object detection model that identifies plant diseases from images. The backend receives images from a Flutter app, processes them using the model, and returns the detection results along with confidence scores.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Model Details](#model-details)
- [Contributing](#contributing)
- [License](#license)

## Features

- Receives plant images from a Flutter app.
- Runs an object detection model to identify plant diseases.
- Returns detection results with confidence scores.
- Built with Flask for ease of deployment and scalability.

## Installation

To get started with the backend, follow these steps to setup locally:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/ChrisKusi/plant_disease_backend.git
    cd plant_disease_backend
    ```

2. **Set up a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**
    Create a `.env` file in the project root and add the necessary configuration variables. Example:
    ```env
    FLASK_APP=app.py
    FLASK_ENV=development
    ```

5. **Run the Flask app:**
    ```bash
    python app.py --host=0.0.0.0
    ```

## Usage

Once the server is running, it will be ready to receive images from the Flutter app. Ensure the Flutter app is configured to send images to the correct endpoint.

## API Endpoints

### POST /detect

**Description:** This endpoint receives an image, processes it using the object detection model, and returns the detection results along with confidence scores.

- **URL:** `/detect`
- **Method:** `POST`
- **Headers:** `Content-Type: multipart/form-data`
- **Body:**
  - `image`: The image file to be processed.

**Response:**
- **Status Code:** `200 OK`
- **Body:**
  ```json
  {
    "detections": [
      {
        "disease": "Leaf Blight",
        "confidence": 0.95
      },
      {
        "disease": "Powdery Mildew",
        "confidence": 0.89
      }
    ]
  }



## Model Details
    The object detection model used in this project is trained to identify various plant diseases from images. Details on the model architecture, training data, and performance can be provided here.

## Example Model Architecture:
    Model: YOLOv8
    Input Size: 640x640
    Output: Bounding boxes with disease labels and confidence scores
    Training Data:
    Dataset: Custom dataset with annotated images of plant diseases.
    Classes: Leaf Blight, Powdery Mildew, Rust, etc.
    Performance:
    Accuracy: 92%
    Precision: 90%
    Recall: 88%

## Contributing
    We welcome contributions to improve this project. If you would like to contribute, please follow these steps:

    1. Fork the repository.
    2. Create a new branch (git checkout -b feature/your-feature-name).
    3. Make your changes.
    4. Commit your changes (git commit -m 'Add some feature').
    5. Push to the branch (git push origin feature/your-feature-name).
    6. Open a Pull Request.


## License
    This project is licensed under the MIT License. See the LICENSE file for details.


Feel free to customize this `README.md` further based on specific details of your project. If you need additional sections or modifications, let me know!
