# TextToEmotion - Emotion Prediction System

[![Deployed](https://img.shields.io/badge/deployed-yes-brightgreen)](https://text-to-emotion-prediction-website.onrender.com)

TextToEmotion is an advanced natural language processing (NLP) web application that analyzes text input to predict and visualize emotional content. The system uses machine learning to identify and categorize emotions in text, providing valuable insights into sentiment and emotional tone.

## Features

- **Multi-Emotion Detection**: Supports prediction of six distinct emotions: sadness, anger, love, surprise, fear, and happiness
- **Natural Language Processing**: Utilizes spaCy for advanced text processing and part-of-speech tagging
- **Interactive Visualization**: Displays emotion distribution through an interactive pie chart
- **Real-time Analysis**: Provides instant emotion predictions for user input
- **RESTful API**: Includes a POST endpoint for programmatic text analysis

## Technical Overview

### Architecture

The system consists of:
- A Flask web server providing RESTful endpoints
- A Decision Tree Classifier for emotion prediction
- A preprocessing pipeline using spaCy for NLP
- A visualization layer using Chart.js

### Data Processing Pipeline

1. Text Input → spaCy Processing → Part-of-Speech Tagging
2. Feature Extraction → Decision Tree Model → Emotion Prediction
3. Results Visualization → Pie Chart Display

## Setup and Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd TextToEmotionPredictionModel
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Start the server:
```bash
python app.py
```

The application will be available at http://localhost:5000

## Usage

1. **Web Interface**
   - Visit the deployed website or local server
   - Enter text in the input box
   - Click "Analyze" to see emotion distribution

2. **API Usage**
   POST request to `/analyze` with form data:
   ```json
   {
     "user_text": "Your text to analyze"
   }
   ```

## Technologies Used

- **Backend**
  - Flask 3.1.0
  - Python 3.8+
  - spaCy 3.8.3
  - scikit-learn 1.6.0

- **Frontend**
  - HTML5
  - Chart.js 4.4.7
  - Bootstrap 5

- **Machine Learning**
  - Decision Tree Classifier
  - Pandas for data processing
  - NumPy for numerical operations

## Model Architecture

The emotion prediction model uses a Decision Tree Classifier trained on a dataset of labeled emotions. The preprocessing pipeline includes:
- Text normalization
- Part-of-speech tagging
- Feature extraction focusing on VERB, ADJ, ADV, and NOUN tokens
- Vectorization of text features

