# Customer-feedback-analysis (NLP + Dashboard)

## Overview

Customer Feedback Analyzer is a full-stack NLP-based system that analyzes customer reviews and provides:

* Sentiment classification (Positive / Negative / Neutral)
* Confidence score
* Keyword extraction
* Actionable business insights
* Real-time analytics dashboard

This project combines Machine Learning, NLP, and a React-based dashboard to simulate a real-world business intelligence system.

---

## Features

* Sentiment Analysis using Machine Learning (Naive Bayes)
* Interactive Dashboard (React + Chart.js)
* Keyword Extraction (Business-relevant terms)
* Insight Generation (Actionable suggestions)
* Dynamic Graphs (Confidence & Sentiment Distribution)
* Real-time API communication (Flask backend)

---

## Tech Stack

### Frontend

* React.js
* Chart.js
* Axios

### Backend

* Flask (Python)
* Scikit-learn
* NLTK

### Machine Learning

* TF-IDF Vectorization
* Multinomial Naive Bayes

---

## How It Works

1. User enters customer feedback
2. Backend preprocesses text (cleaning and stopword removal)
3. TF-IDF converts text into numerical features
4. ML model predicts sentiment
5. System extracts keywords and generates insights
6. Results are displayed on the dashboard with graphs

---

## Output Example

### Input:

```id="8c9l2p"
The service was excellent and the product quality is really good, but delivery was slow
```

### Output:

* Sentiment: Positive
* Confidence: 72%
* Keywords: service, product, delivery
* Insights:

  * Improve delivery speed
  * Maintain product quality
  * Improve customer service

---

## Project Structure

```id="r3z7nb"
customer_feedback_analyzer/
│
├── backend/
│   └── app.py
│
├── frontend/
│   └── src/
│       ├── App.js
│       └── components/
│           └── Dashboard.js
│
└── README.md
```

---

## Installation and Setup

### Backend Setup

```bash id="k2u8fh"
cd backend
pip install flask flask-cors nltk scikit-learn pandas numpy
python app.py
```

---

### Frontend Setup

```bash id="n5v1rk"
cd frontend
npm install
npm install axios chart.js react-chartjs-2
npm start
```

---

## Dashboard Features

* Sentiment Display (color-coded)
* Confidence Visualization (bar chart)
* Sentiment Distribution (pie chart)
* Keywords and Insights section

---

## Key Concepts Used

* Natural Language Processing (NLP)
* Text Preprocessing
* Feature Extraction (TF-IDF)
* Machine Learning Classification
* Data Visualization

---

## Limitations

* Uses a small dataset (prototype level)
* Confidence scores are relative, not absolute
* Not trained on large real-world datasets

---

## Future Enhancements

* Use larger datasets for better accuracy
* Implement deep learning models such as BERT
* Add CSV upload for bulk feedback analysis
* Deploy as a full-scale web application

---

## Conclusion

This project demonstrates how NLP and Machine Learning can be used to convert unstructured customer feedback into meaningful insights and actionable decisions using an interactive dashboard.
