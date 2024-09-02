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
#             'image_url': f"http://{request.host}/processed/{processed_filename}"
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


# saving user data to json

# from flask import Flask, request, jsonify, send_from_directory
# from werkzeug.utils import secure_filename
# import os
# import uuid
# import cv2
# import numpy as np
# from ultralytics import YOLO
# import logging
# import json


# app = Flask(__name__)

# USER_DATA_FILE = 'user_data.json'
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
#             'image_url': f"http://{request.host}/processed/{processed_filename}"
#         }
#         logging.debug('Detection successful, sending response')
#         return jsonify(response)
#     except Exception as e:
#         logging.error(f'Error during detection: {e}')
#         return jsonify({'error': str(e)}), 500

# @app.route('/processed/<filename>')
# def processed_image(filename):
#     return send_from_directory(app.config['PROCESSED_FOLDER'], filename)


# def load_user_data():
#     if os.path.exists(USER_DATA_FILE):
#         with open(USER_DATA_FILE, 'r') as file:
#             return json.load(file)
#     return {}

# def save_user_data(data):
#     with open(USER_DATA_FILE, 'w') as file:
#         json.dump(data, file)

# @app.route('/get_user_data', methods=['GET'])
# def get_user_data():
#     logging.debug('Received request for /get_user_data')
#     try:
#         user_data = load_user_data()
#         logging.debug('User data retrieved successfully')
#         return jsonify(user_data)
#     except Exception as e:
#         logging.error(f'Error retrieving user data: {e}')
#         return jsonify({'error': str(e)}), 500

# @app.route('/save_user_data', methods=['POST'])
# def save_user_data_route():
#     logging.debug('Received request for /save_user_data')
#     try:
#         user_data = request.json
#         save_user_data(user_data)
#         logging.debug('User data saved successfully')
#         return jsonify({'status': 'success'})
#     except Exception as e:
#         logging.error(f'Error saving user data: {e}')
#         return jsonify({'error': str(e)}), 500

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)


# email


# from flask import Flask, request, jsonify, send_from_directory
# from werkzeug.utils import secure_filename
# import os
# import uuid
# import cv2
# import numpy as np
# from ultralytics import YOLO
# import logging
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.base import MIMEBase
# from email import encoders
# from email_validator import validate_email, EmailNotValidError
# from PIL import Image
# from PIL.ExifTags import TAGS, GPSTAGS
# import json

# app = Flask(__name__)

# UPLOAD_FOLDER = 'uploads'
# PROCESSED_FOLDER = 'processed'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER

# if not os.path.exists(UPLOAD_FOLDER):
#     os.makedirs(UPLOAD_FOLDER)

# if not os.path.exists(PROCESSED_FOLDER):
#     os.makedirs(PROCESSED_FOLDER)

# USER_DATA_FILE = 'user_data.json'

# # Enable logging
# logging.basicConfig(level=logging.DEBUG)

# # Load the YOLOv8 model
# model = YOLO('models/best.pt')

# def load_user_data():
#     if os.path.exists(USER_DATA_FILE):
#         with open(USER_DATA_FILE, 'r') as file:
#             return json.load(file)
#     return {}

# def save_user_data(data):
#     with open(USER_DATA_FILE, 'w') as file:
#         json.dump(data, file)

# def extract_metadata(image_path):
#     image = Image.open(image_path)
#     info = image._getexif()
#     metadata = {}
#     if info:
#         for tag, value in info.items():
#             tag_name = TAGS.get(tag, tag)
#             if tag_name == 'GPSInfo':
#                 gps_info = {}
#                 for t in value:
#                     sub_tag = GPSTAGS.get(t, t)
#                     gps_info[sub_tag] = value[t]
#                 metadata[tag_name] = gps_info
#             else:
#                 metadata[tag_name] = value
#     return metadata

# def convert_to_degrees(value):
#     d = float(value[0])
#     m = float(value[1])
#     s = float(value[2])
#     return d + (m / 60.0) + (s / 3600.0)

# def get_lat_lon(metadata):
#     if 'GPSInfo' not in metadata:
#         return None, None
#     gps_info = metadata['GPSInfo']
#     gps_latitude = gps_info.get('GPSLatitude')
#     gps_latitude_ref = gps_info.get('GPSLatitudeRef')
#     gps_longitude = gps_info.get('GPSLongitude')
#     gps_longitude_ref = gps_info.get('GPSLongitudeRef')

#     if not gps_latitude or not gps_longitude:
#         return None, None

#     lat = convert_to_degrees(gps_latitude)
#     lon = convert_to_degrees(gps_longitude)

#     if gps_latitude_ref != 'N':
#         lat = -lat
#     if gps_longitude_ref != 'E':
#         lon = -lon

#     return lat, lon

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

# def send_email(to_email, subject, body, attachment_path):
#     from_email = "kusichris656@gmail.com"
#     from_password = "ksacvljysbzrxqzl"

#     # Create the email
#     msg = MIMEMultipart()
#     msg['From'] = from_email
#     msg['To'] = to_email
#     msg['Subject'] = subject

#     # Attach the body with the msg instance
#     msg.attach(MIMEText(body, 'plain'))

#     # Open the file to be sent
#     attachment = open(attachment_path, "rb")

#     # Instance of MIMEBase and named as p
#     p = MIMEBase('application', 'octet-stream')

#     # To change the payload into encoded form
#     p.set_payload(attachment.read())

#     # Encode into base64
#     encoders.encode_base64(p)

#     p.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(attachment_path)}")

#     # Attach the instance 'p' to instance 'msg'
#     msg.attach(p)

#     # Create SMTP session
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.starttls()
#     server.login(from_email, from_password)

#     # Send the email
#     server.sendmail(from_email, to_email, msg.as_string())
#     server.quit()

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

#         # Extract metadata and location
#         metadata = extract_metadata(file_path)
#         lat, lon = get_lat_lon(metadata)
#         google_maps_link = f"https://www.google.com/maps?q={lat},{lon}" if lat and lon else "Location not available"

#         # Load user data
#         user_data = load_user_data()
#         email = user_data.get('email')
#         name = user_data.get('name')

#         # Prepare email
#         if email:
#             subject = "Plant Disease Detection Report"
#             body = f"""
#             Dear {name},

#             Here is the detection report for the image you uploaded:

#             Disease: {detections[0]['class_name']}
#             Confidence: {detections[0]['confidence']:.2f}
#             Location: {google_maps_link}

#             Attached is the processed image with the detections highlighted.

#             Best regards,
#             Your Plant Disease Detection Team
#             """
#             send_email(email, subject, body, processed_file_path)

#         response = {
#             'detections': detections,
#             'image_url': f"http://{request.host}/processed/{processed_filename}",
#             'location': google_maps_link
#         }
#         logging.debug('Detection successful, sending response')
#         return jsonify(response)
#     except Exception as e:
#         logging.error(f'Error during detection: {e}')
#         return jsonify({'error': str(e)}), 500

# @app.route('/processed/<filename>')
# def processed_image(filename):
#     return send_from_directory(app.config['PROCESSED_FOLDER'], filename)

# @app.route('/get_user_data', methods=['GET'])
# def get_user_data():
#     logging.debug('Received request for /get_user_data')
#     try:
#         user_data = load_user_data()
#         logging.debug('User data retrieved successfully')
#         return jsonify(user_data)
#     except Exception as e:
#         logging.error(f'Error retrieving user data: {e}')
#         return jsonify({'error': str(e)}), 500

# @app.route('/save_user_data', methods=['POST'])
# def save_user_data_route():
#     logging.debug('Received request for /save_user_data')
#     try:
#         user_data = request.json
#         save_user_data(user_data)
#         logging.debug('User data saved successfully')
#         return jsonify({'status': 'success'})
#     except Exception as e:
#         logging.error(f'Error saving user data: {e}')
#         return jsonify({'error': str(e)}), 500

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)


# email 2 location

# from flask import Flask, request, jsonify, send_from_directory
# from werkzeug.utils import secure_filename
# import os
# import uuid
# import cv2
# import numpy as np
# from ultralytics import YOLO
# import logging
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.base import MIMEBase
# from email import encoders
# from email_validator import validate_email, EmailNotValidError
# from PIL import Image
# from PIL.ExifTags import TAGS
# import json

# app = Flask(__name__)

# UPLOAD_FOLDER = 'uploads'
# PROCESSED_FOLDER = 'processed'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER

# if not os.path.exists(UPLOAD_FOLDER):
#     os.makedirs(UPLOAD_FOLDER)

# if not os.path.exists(PROCESSED_FOLDER):
#     os.makedirs(PROCESSED_FOLDER)

# USER_DATA_FILE = 'user_data.json'

# # Enable logging
# logging.basicConfig(level=logging.DEBUG)

# # Load the YOLOv8 model
# model = YOLO('models/best.pt')

# def load_user_data():
#     if os.path.exists(USER_DATA_FILE):
#         with open(USER_DATA_FILE, 'r') as file:
#             return json.load(file)
#     return {}

# def save_user_data(data):
#     with open(USER_DATA_FILE, 'w') as file:
#         json.dump(data, file)

# def extract_metadata(image_path):
#     image = Image.open(image_path)
#     info = image._getexif()
#     metadata = {}
#     if info:
#         for tag, value in info.items():
#             tag_name = TAGS.get(tag, tag)
#             metadata[tag_name] = value
#     return metadata

# def extract_location(metadata):
#     if 'ImageDescription' in metadata:
#         location = metadata['ImageDescription']
#         # Assuming the location format is similar to the screenshot provided
#         return location
#     return "Location not available"

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

# def send_email(to_email, subject, body, attachment_path):
#     from_email = "kusichris656@gmail.com"
#     from_password = "ksacvljysbzrxqzl"

#     # Create the email
#     msg = MIMEMultipart()
#     msg['From'] = from_email
#     msg['To'] = to_email
#     msg['Subject'] = subject

#     # Attach the body with the msg instance
#     msg.attach(MIMEText(body, 'plain'))

#     # Open the file to be sent
#     attachment = open(attachment_path, "rb")

#     # Instance of MIMEBase and named as p
#     p = MIMEBase('application', 'octet-stream')

#     # To change the payload into encoded form
#     p.set_payload(attachment.read())

#     # Encode into base64
#     encoders.encode_base64(p)

#     p.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(attachment_path)}")

#     # Attach the instance 'p' to instance 'msg'
#     msg.attach(p)

#     # Create SMTP session
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.starttls()
#     server.login(from_email, from_password)

#     # Send the email
#     server.sendmail(from_email, to_email, msg.as_string())
#     server.quit()

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

#         # Extract metadata and location
#         metadata = extract_metadata(file_path)
#         location = extract_location(metadata)
#         google_maps_link = f"https://www.google.com/maps/place/{location.replace(' ', '+')}" if location else "Location not available"

#         # Load user data
#         user_data = load_user_data()
#         email = user_data.get('email')
#         name = user_data.get('name')

#         # Prepare email
#         if email:
#             subject = "Plant Disease Detection Report"
#             body = f"""
#             Dear {name},

#             Here is the detection report for the image you uploaded:

#             Disease: {detections[0]['class_name']}
#             Confidence: {detections[0]['confidence']:.2f}
#             Location: {google_maps_link}

#             Attached is the processed image with the detections highlighted.

#             Best regards,
#             Your Plant Disease Detection Team
#             """
#             send_email(email, subject, body, processed_file_path)

#         response = {
#             'detections': detections,
#             'image_url': f"http://{request.host}/processed/{processed_filename}",
#             'location': google_maps_link
#         }
#         logging.debug('Detection successful, sending response')
#         return jsonify(response)
#     except Exception as e:
#         logging.error(f'Error during detection: {e}')
#         return jsonify({'error': str(e)}), 500

# @app.route('/processed/<filename>')
# def processed_image(filename):
#     return send_from_directory(app.config['PROCESSED_FOLDER'], filename)

# @app.route('/get_user_data', methods=['GET'])
# def get_user_data():
#     logging.debug('Received request for /get_user_data')
#     try:
#         user_data = load_user_data()
#         logging.debug('User data retrieved successfully')
#         return jsonify(user_data)
#     except Exception as e:
#         logging.error(f'Error retrieving user data: {e}')
#         return jsonify({'error': str(e)}), 500

# @app.route('/save_user_data', methods=['POST'])
# def save_user_data_route():
#     logging.debug('Received request for /save_user_data')
#     try:
#         user_data = request.json
#         save_user_data(user_data)
#         logging.debug('User data saved successfully')
#         return jsonify({'status': 'success'})
#     except Exception as e:
#         logging.error(f'Error saving user data: {e}')
#         return jsonify({'error': str(e)}), 500

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
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email_validator import validate_email, EmailNotValidError
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import json
from geopy.geocoders import Nominatim

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
PROCESSED_FOLDER = 'processed'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

if not os.path.exists(PROCESSED_FOLDER):
    os.makedirs(PROCESSED_FOLDER)

USER_DATA_FILE = 'user_data.json'

# Enable logging
logging.basicConfig(level=logging.DEBUG)

# Load the YOLOv8 model
model = YOLO('models/best.pt')

def load_user_data():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_user_data(data):
    with open(USER_DATA_FILE, 'w') as file:
        json.dump(data, file)

def extract_metadata(image_path):
    image = Image.open(image_path)
    info = image._getexif()
    metadata = {}
    if info:
        for tag, value in info.items():
            tag_name = TAGS.get(tag, tag)
            metadata[tag_name] = value
    return metadata

def extract_location(metadata):
    if 'GPSInfo' in metadata:
        gps_info = metadata['GPSInfo']
        def dms_to_decimal(degrees, minutes, seconds, direction):
            decimal_degrees = float(degrees) + (float(minutes) / 60) + (float(seconds) / 3600)
            if direction in ['S', 'W']:
                decimal_degrees *= -1
            return decimal_degrees
        
        gps_lat = gps_info[2]
        gps_lon = gps_info[4]
        lat = dms_to_decimal(gps_lat[0], gps_lat[1], gps_lat[2], gps_info[1])
        lon = dms_to_decimal(gps_lon[0], gps_lon[1], gps_lon[2], gps_info[3])
        geolocator = Nominatim(user_agent="metadata/1.0")
        location = geolocator.reverse(f"{lat}, {lon}")
        return location.address if location else "Location not available"
    return "Location not available"

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

def send_email(to_email, subject, body, attachment_path):
    from_email = "leafscan0@gmail.com"
    from_password = "vjcyoihxxcomqqga"

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # Open the file to be sent
    attachment = open(attachment_path, "rb")

    # Instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    p.set_payload(attachment.read())

    # Encode into base64
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(attachment_path)}")

    # Attach the instance 'p' to instance 'msg'
    msg.attach(p)

    # Create SMTP session
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, from_password)

    # Send the email
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()

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

#         # Extract metadata and location
#         metadata = extract_metadata(file_path)
#         location = extract_location(metadata)
#         google_maps_link = f"https://www.google.com/maps/place/{location.replace(' ', '+')}" if location else "Location not available"

#         # Load user data
#         user_data = load_user_data()
#         email = user_data.get('email')
#         name = user_data.get('name')

#         # Prepare email
#         if email:
#             subject = "Plant Disease Detection Report"
#             body = f"""
#             Dear {name},

#             Here is the detection report for the image you uploaded:

#             Disease: {detections[0]['class_name']}
#             Confidence: {detections[0]['confidence']:.2f}
#             Location: {location}
#             Google Maps Link: {google_maps_link}

#             Attached is the processed image with the detections highlighted.

#             Best regards,
#             Your Plant Disease Detection Team
#             """
#             send_email(email, subject, body, processed_file_path)

#         response = {
#             'detections': detections,
#             'image_url': f"http://{request.host}/processed/{processed_filename}",
#             'location': location,
#             'google_maps_link': google_maps_link
#         }
#         logging.debug('Detection successful, sending response')
#         return jsonify(response)
#     except Exception as e:
#         logging.error(f'Error during detection: {e}')
#         return jsonify({'error': str(e)}), 500

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

        # Extract metadata and location (if EXIF data is used)
        metadata = extract_metadata(file_path)
        location = extract_location(metadata) or "Location not available"

        # Handle provided location data
        latitude = request.form.get('latitude')
        longitude = request.form.get('longitude')
        if latitude and longitude:
            location = f"Lat: {latitude}, Long: {longitude}"
            google_maps_link = f"https://www.google.com/maps/place/{latitude},{longitude}"
        else:
            google_maps_link = "Location not available"

        # Load user data
        user_data = load_user_data()
        email = user_data.get('email')
        name = user_data.get('name')

        # Prepare and send email with location data included
        if email:
            subject = "Plant Disease Detection Report"
            body = f"""
            Dear {name},

            Here is the detection report for the image you uploaded:

            Disease: {detections[0]['class_name']}
            Confidence: {detections[0]['confidence']:.2f}
            Location: {location}
            Google Maps Link: {google_maps_link}

            Attached is the processed image with the detections highlighted.

            Best regards,
            Your Plant Disease Detection Team
            """
            send_email(email, subject, body, processed_file_path)

        response = {
            'detections': detections,
            'image_url': f"http://{request.host}/processed/{processed_filename}",
            'location': location,
            'google_maps_link': google_maps_link
        }
        logging.debug('Detection successful, sending response')
        return jsonify(response)
    except Exception as e:
        logging.error(f'Error during detection: {e}')
        return jsonify({'error': str(e)}), 500


@app.route('/processed/<filename>')
def processed_image(filename):
    return send_from_directory(app.config['PROCESSED_FOLDER'], filename)

@app.route('/get_user_data', methods=['GET'])
def get_user_data():
    logging.debug('Received request for /get_user_data')
    try:
        user_data = load_user_data()
        logging.debug('User data retrieved successfully')
        return jsonify(user_data)
    except Exception as e:
        logging.error(f'Error retrieving user data: {e}')
        return jsonify({'error': str(e)}), 500

@app.route('/save_user_data', methods=['POST'])
def save_user_data_route():
    logging.debug('Received request for /save_user_data')
    try:
        user_data = request.json
        save_user_data(user_data)
        logging.debug('User data saved successfully')
        return jsonify({'status': 'success'})
    except Exception as e:
        logging.error(f'Error saving user data: {e}')
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
