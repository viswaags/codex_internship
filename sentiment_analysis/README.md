# 📊 Sentiment Analysis Web App

This is a minimal Flask web application that performs **sentiment analysis** on user input using **TextBlob**. It detects sentiment polarity, subjectivity, and suggests an appropriate emoji based on the sentiment.

## ✨ Features

- Analyzes sentiment (Positive / Negative / Neutral)
- Displays polarity and subjectivity scores
- Suggests an emoji based on text meaning and sentiment
- Simple, modern UI built with HTML/CSS/JS

## 📦 Requirements

Create and activate a virtual environment first (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Then download TextBlob corpora:

```bash
python -m textblob.download_corpora
```

## 🛠️ How to Run

```bash
python app.py
```

Then open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

## 📁 File Structure

```
├── app.py                 # Flask backend
├── templates/
│   └── app.html           # Frontend HTML
├── static/
│   ├── app.css          # Optional CSS
│   └── app.js          # Optional JS
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## 📚 Tech Stack

- **Backend**: Python, Flask, TextBlob
- **Frontend**: HTML, CSS (custom), JS (optional)
- **Sentiment Engine**: TextBlob (NLTK-based)

## 📄 License

This project is for learning purposes and open to contributions.