from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

def suggest_emoji(text, sentiment):
    text_lower = text.lower()
    if sentiment == 'Positive':
        if 'love' in text_lower or 'like' in text_lower:
            return '😍'
        elif 'win' in text_lower or 'congrats' in text_lower:
            return '🎉'
        elif 'happy' in text_lower or 'smile' in text_lower:
            return '😁'
        else:
            return '😊'
    elif sentiment == 'Negative':
        if 'hate' in text_lower or 'angry' in text_lower:
            return '😡'
        elif 'sad' in text_lower or 'cry' in text_lower:
            return '😭'
        elif 'bad' in text_lower or 'worst' in text_lower:
            return '👎'
        else:
            return '😢'
    else:
        if 'hmm' in text_lower or 'okay' in text_lower:
            return '🤔'
        elif 'nothing' in text_lower:
            return '😶'
        else:
            return '😐'

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = polarity = subjectivity = emoji = None
    if request.method == 'POST':
        text = request.form['text']
        blob = TextBlob(text)
        polarity = round(blob.sentiment.polarity, 2)
        subjectivity = round(blob.sentiment.subjectivity, 2)
        if polarity > 0:
            sentiment = 'Positive'
        elif polarity < 0:
            sentiment = 'Negative'
        else:
            sentiment = 'Neutral'
        emoji = suggest_emoji(text, sentiment)

    return render_template('app.html',
                           sentiment=sentiment,
                           polarity=polarity,
                           subjectivity=subjectivity,
                           emoji=emoji)

if __name__ == '__main__':
    app.run(debug=True)
