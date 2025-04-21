from flask import Flask, request, jsonify, render_template
import joblib
import logging
import os
from tensorflow.keras.models import load_model

# Set up logging
logging.basicConfig(level=logging.INFO)

# Load the trained model and TF-IDF vectorizer
try:
    model = load_model('drug_trafficking_model_with_augmentation_new.h5')
    vectorizer = joblib.load('tfidf_vectorizer.pkl')
    logging.info("Model and vectorizer loaded successfully.")
except Exception as e:
    logging.error(f"Error loading model or vectorizer: {str(e)}")

# Set up Flask app and template folder to the current directory
app = Flask(__name__, template_folder=os.getcwd())
app.config['JSON_AS_ASCII'] = False  # Allow non-ASCII characters in JSON responses

@app.route('/')
def home():
    # Render the updated HTML template for input, which is in the same folder as the app
    return render_template('nlp_index.html')  # Make sure nlp_index.html is in the same folder as this script

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the comment from the form submission
        comment = request.form.get('comment', '').strip()

        # Log received comment
        logging.info(f"Received comment: {comment}")

        # Check if the comment is empty
        if not comment:
            logging.warning("Received empty comment.")
            return jsonify({'error': 'Comment cannot be empty.'}), 400
        
        # Transform the comment using the TF-IDF vectorizer
        comment_tfidf = vectorizer.transform([comment]).toarray()
        logging.info(f"Transformed comment TF-IDF: {comment_tfidf}")

        # Predict with the model
        prediction = model.predict(comment_tfidf)
        logging.info(f"Model prediction output: {prediction}")

        # Apply a threshold for classification (adjustable)
        result = 1 if prediction[0][0] > 0.5 else 0
        logging.info(f"Prediction result: {result}")

        # Return the prediction result as a JSON response
        return jsonify({'prediction': result})
    
    except Exception as e:
        logging.error(f"Error occurred during prediction: {str(e)}")
        return jsonify({'error': 'An error occurred during prediction.'}), 500

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)  # Disable reloading to avoid WebSocket interference
