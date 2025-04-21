
# 🚀 Drugs Trafficking Website using NLP and CNN
# 🧠 A smart detection system combining NLP and CNN to identify drug content from text and images.


Welcome to my Drugs Trafficking Website project!
This application can detect drug-related texts and images using AI models trained with real-world datasets.

# The project combines:

Natural Language Processing (NLP) for text analysis.

Convolutional Neural Networks (CNN) for image classification.

A Flask backend connected to a simple HTML/CSS/JS frontend.

# ✨ Key Features
🔍 Detect drug-related text content.

🖼️ Detect drug-related images.

⚡ Real-time AI predictions.

🌐 Simple and clean web interface.

📂 Custom datasets built and trained from scratch.

# 🛠️ Technologies Used
Python (Flask, TensorFlow/Keras, Scikit-learn)

NLP (Text cleaning, TF-IDF, Logistic Regression/SVM)

CNN (Deep Learning for Image Classification)

Instagram Graph API (for real-world text data)

HTML / CSS / JavaScript (Frontend)

VS Code (Local Development)

Google Colab (Model Training)

# 📈 Project Workflow
# 📖 Text Dataset (NLP)
Extracted Instagram captions using the Instagram Graph API.

Processed and labeled the text for drug-related vs non-drug-related classification.

Saved in a structured dataset for training the NLP model.

# 🖼️ Image Dataset (CNN)
Collected images manually from trusted sources.

Created two categories: Drug-Related and Non-Drug-Related.

Applied data augmentation (rotation, flipping, zooming) to expand the dataset.

Used for CNN model training.

# 🤖 Model Training
# NLP Model:

Preprocessing: Cleaning text, tokenization, TF-IDF vectorization.

Trained using Logistic Regression/SVM classifiers on local VS Code.

# CNN Model:

# Architecture: Convolutional Layers + MaxPooling + Dense layers.

Trained on Google Colab using GPU for faster computation.

# 🌍 How It Works
User uploads a text or image on the website.

Flask backend processes the input:

Text is passed through the NLP model.

Image is passed through the CNN model.

The AI models predict whether the content is drug-related or not.

The prediction is displayed instantly on the frontend.

# 🎯 Future Enhancements
📊 Add a dashboard to visualize predictions.

🚀 Deploy the app to a cloud platform (AWS, Render, Vercel).

🔐 Add user authentication and logging.

🧠 Train models with larger, more diverse datasets.

🌟 Thank you for visiting this project!
