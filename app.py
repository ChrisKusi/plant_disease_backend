# from flask import Flask, request, jsonify
# import numpy as np
# import cv2
# from ultralytics import YOLO
# import base64
# import io
# from PIL import Image
# import logging

# app = Flask(__name__)

# # Enable logging
# logging.basicConfig(level=logging.DEBUG)

# # Load the YOLOv8 model
# model = YOLO('models/best.pt')

# def detect_disease(image):
#     # Use YOLOv8 model to detect diseases
#     results = model(image)
#     return results

# def draw_detections(image, results):
#     detections = []
#     for result in results:
#         for box in result.boxes:
#             x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
#             class_id = int(box.cls[0])
#             confidence = float(box.conf[0])
#             label = f"{model.names[class_id]}: {confidence:.2f}"
#             cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)
#             cv2.putText(image, label, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
#             detections.append({
#                 'box': [x1, y1, x2-x1, y2-y1],
#                 'class_id': class_id,
#                 'confidence': confidence
#             })
#     return image, detections

# @app.route('/detect', methods=['POST'])
# def detect():
#     logging.debug('Received request for /detect')
#     try:
#         file = request.files['image']
#         image = np.frombuffer(file.read(), np.uint8)
#         image = cv2.imdecode(image, cv2.IMREAD_COLOR)

#         results = detect_disease(image)
#         image_with_detections, detections = draw_detections(image, results)

#         # Convert image to PNG format
#         _, img_encoded = cv2.imencode('.png', image_with_detections)
#         img_bytes = img_encoded.tobytes()
#         img_base64 = base64.b64encode(img_bytes).decode('utf-8')

#         response = {
#             'image': img_base64,
#             'detections': detections
#         }
#         logging.debug('Detection successful, sending response')
#         return jsonify(response)
#     except Exception as e:
#         logging.error(f'Error during detection: {e}')
#         return jsonify({'error': str(e)}), 500

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)


# from flask import Flask, request, jsonify, send_from_directory
# from werkzeug.utils import secure_filename
# import os
# import uuid
# import cv2
# import numpy as np
# from ultralytics import YOLO
# import logging

# app = Flask(__name__)

# UPLOAD_FOLDER = 'uploads'
# PROCESSED_FOLDER = 'processed'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER

# if not os.path.exists(UPLOAD_FOLDER):
#     os.makedirs(UPLOAD_FOLDER)

# if not os.path.exists(PROCESSED_FOLDER):
#     os.makedirs(PROCESSED_FOLDER)

# # Enable logging
# logging.basicConfig(level=logging.DEBUG)

# # Load the YOLOv8 model
# model = YOLO('models/best.pt')

# def detect_disease(image):
#     # Use YOLOv8 model to detect diseases
#     results = model(image)
#     return results

# def draw_detections(image, results):
#     detections = []
#     for result in results:
#         for box in result.boxes:
#             x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
#             class_id = int(box.cls[0])
#             confidence = float(box.conf[0])
#             label = f"{model.names[class_id]}: {confidence:.2f}"
#             cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)
#             cv2.putText(image, label, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
#             detections.append({
#                 'class_name': model.names[class_id],
#                 'confidence': confidence
#             })
#     return image, detections

# @app.route('/detect', methods=['POST'])
# def detect():
#     logging.debug('Received request for /detect')
#     try:
#         file = request.files['image']
#         filename = secure_filename(file.filename)
#         file_id = str(uuid.uuid4())
#         file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_id + '_' + filename)
#         file.save(file_path)

#         image = cv2.imread(file_path)
#         results = detect_disease(image)
#         image_with_detections, detections = draw_detections(image, results)

#         processed_filename = file_id + '_processed.png'
#         processed_file_path = os.path.join(app.config['PROCESSED_FOLDER'], processed_filename)
#         cv2.imwrite(processed_file_path, image_with_detections)

#         response = {
#             'detections': detections,
#             'image_url': f"http://{request.host}/{app.config['PROCESSED_FOLDER']}/{processed_filename}"
#         }
#         logging.debug('Detection successful, sending response')
#         return jsonify(response)
#     except Exception as e:
#         logging.error(f'Error during detection: {e}')
#         return jsonify({'error': str(e)}), 500

# @app.route('/processed/<filename>')
# def processed_image(filename):
#     return send_from_directory(app.config['PROCESSED_FOLDER'], filename)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)


from flask import Flask, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
import os
import uuid
import cv2
import numpy as np
from ultralytics import YOLO
import logging

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
PROCESSED_FOLDER = 'processed'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

if not os.path.exists(PROCESSED_FOLDER):
    os.makedirs(PROCESSED_FOLDER)

# Enable logging
logging.basicConfig(level=logging.DEBUG)

# Load the YOLOv8 model
model = YOLO('models/best.pt')

def detect_disease(image):
    # Use YOLOv8 model to detect diseases
    results = model(image)
    return results

def draw_detections(image, results):
    detections = []
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
            class_id = int(box.cls[0])
            confidence = float(box.conf[0])
            label = f"{model.names[class_id]}: {confidence:.2f}"
            cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)
            cv2.putText(image, label, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
            detections.append({
                'class_name': model.names[class_id],
                'confidence': confidence
            })
    return image, detections

@app.route('/detect', methods=['POST'])
def detect():
    logging.debug('Received request for /detect')
    try:
        file = request.files['image']
        filename = secure_filename(file.filename)
        file_id = str(uuid.uuid4())
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_id + '_' + filename)
        file.save(file_path)

        image = cv2.imread(file_path)
        results = detect_disease(image)
        image_with_detections, detections = draw_detections(image, results)

        processed_filename = file_id + '_processed.png'
        processed_file_path = os.path.join(app.config['PROCESSED_FOLDER'], processed_filename)
        cv2.imwrite(processed_file_path, image_with_detections)

        response = {
            'detections': detections,
            'image_url': f"http://{request.host}/processed/{processed_filename}"
        }
        logging.debug('Detection successful, sending response')
        return jsonify(response)
    except Exception as e:
        logging.error(f'Error during detection: {e}')
        return jsonify({'error': str(e)}), 500

@app.route('/processed/<filename>')
def processed_image(filename):
    return send_from_directory(app.config['PROCESSED_FOLDER'], filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
