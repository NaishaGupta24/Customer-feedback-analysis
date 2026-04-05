from flask import Flask, request, jsonify
from flask_cors import CORS
import nltk
import string
import pandas as pd
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import numpy as np

nltk.download('stopwords')

app = Flask(__name__)
CORS(app)

# -----------------------------
# DATASET (IMPROVED)
# -----------------------------
data = {
    "text": [
        "The product is amazing and works great",
        "Absolutely loved it fantastic quality",
        "Very happy with the purchase",
        "Worst product ever very disappointed",
        "Delivery was slow and frustrating",
        "Terrible experience will not buy again",
        "Product is okay nothing special",
        "Average quality acceptable",
        "Not bad but could be better",
        "Excellent service and fast delivery",
        "Horrible packaging and broken item",
        "Good but delivery delay",
        "Bad quality and waste of money",
        "Really impressed with the product",
        "Neutral experience overall",
        "Very bad service and worst support",
        "Amazing product and great service",
        "Slow delivery and poor packaging",
        "Totally waste of money very bad",
        "Satisfied with the quality"
    ],
    "label": [
        "positive","positive","positive",
        "negative","negative","negative",
        "neutral","neutral","neutral",
        "positive","negative","neutral",
        "negative","positive","neutral",
        "negative","positive","negative",
        "negative","positive"
    ]
}

df = pd.DataFrame(data)

# -----------------------------
# PREPROCESSING
# -----------------------------
stop_words = set(stopwords.words('english'))

def preprocess(text):
    text = text.lower()
    text = ''.join([c for c in text if c.isalnum() or c.isspace()])
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return ' '.join(words)

df["clean_text"] = df["text"].apply(preprocess)

# -----------------------------
# MODEL
# -----------------------------
vectorizer = TfidfVectorizer(ngram_range=(1,2))
X = vectorizer.fit_transform(df["clean_text"])
y = df["label"]

model = MultinomialNB()
model.fit(X, y)

# -----------------------------
# HISTORY
# -----------------------------
history = []

# -----------------------------
# SMART KEYWORD EXTRACTION
# -----------------------------
def extract_keywords(text):
    text = text.lower()

    keywords = []

    if "delivery" in text:
        keywords.append("delivery")

    if "service" in text:
        keywords.append("service")

    if "product" in text:
        keywords.append("product")

    if "quality" in text:
        keywords.append("quality")

    if "money" in text or "waste" in text:
        keywords.append("pricing")

    if "slow" in text:
        keywords.append("slow")

    if "bad" in text or "worst" in text:
        keywords.append("negative experience")

    return keywords[:3]

# -----------------------------
# INSIGHT ENGINE (STRONG)
# -----------------------------
def generate_insights(text, sentiment):
    text = text.lower()
    insights = []

    if "delivery" in text:
        insights.append("Improve delivery speed")

    if "service" in text:
        insights.append("Improve customer service")

    if "product" in text or "quality" in text:
        insights.append("Maintain product quality")

    if "money" in text or "waste" in text:
        insights.append("Pricing or value needs improvement")

    if sentiment == "negative":
        insights.append("Immediate attention required")

    return insights

# -----------------------------
# ROUTES
# -----------------------------
@app.route("/")
def home():
    return "Backend running ✅"

@app.route("/analyze", methods=["POST"])
def analyze():
    text = request.json["text"]

    clean = preprocess(text)
    vec = vectorizer.transform([clean])

    pred = model.predict(vec)[0]
    prob = model.predict_proba(vec)[0]
    confidence = round(float(max(prob)), 2)

    keywords = extract_keywords(text)
    insights = generate_insights(text, pred)

    history.append(pred)

    return jsonify({
        "sentiment": pred,
        "confidence": confidence,
        "keywords": keywords,
        "insights": insights,
        "history": history
    })

if __name__ == "__main__":
    app.run(debug=True)