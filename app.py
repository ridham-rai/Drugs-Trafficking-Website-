from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import logging

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Load the trained model
try:
    model = tf.keras.models.load_model('drug_model.h5')  # Ensure the correct model path
    logging.info("Model loaded successfully.")
except Exception as e:
    logging.error(f"Error loading model: {e}")
    model = None

# Define class labels (assuming binary classification for drug detection)
class_labels = {0: 'Non-Drug', 1: 'Drug'}

# Preprocessing function
def prepare_image(img):
    IMG_SIZE = 150  # Set the image size to 150x150
    img = Image.open(io.BytesIO(img)).convert('RGB')  # Convert image to RGB
    img = img.resize((IMG_SIZE, IMG_SIZE))
    img_array = np.array(img) / 255.0  # Normalize the pixel values
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

@app.route('/')
def index():
    return "Welcome to the Drug Detection API!"

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if not file.content_type.startswith('image/'):
        return jsonify({'error': 'Invalid file type'}), 400

    try:
        # Read and preprocess the image
        img = file.read()
        img_array = prepare_image(img)

        # Ensure the model is loaded
        if model is None:
            return jsonify({'error': 'Model is not available'}), 500

        # Predict using the model
        predictions = model.predict(img_array)
        binary_prediction = (predictions > 0.5).astype(int)

        # Get the class name using the class_labels dictionary
        class_name = class_labels.get(binary_prediction[0][0], 'Unknown')

        # Prepare the response
        return jsonify({
            'prediction': class_name,
            'confidence': float(predictions[0][0]),  # Confidence score
            'raw_output': predictions.tolist()  # Raw output (probabilities)
        })
    except Exception as e:
        logging.error(f"Error during prediction: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
