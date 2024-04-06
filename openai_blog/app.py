from flask import Flask, jsonify
from scraper import fetch_articles
from sentiment_analysis import analyze_sentiment

app = Flask(__name__)

@app.route('/get_data')
def get_data():
    fetch_articles('https://openai.com/blog')  # Effectue le scraping
    return jsonify("Data scraped")

@app.route('/articles')
def articles():
    return jsonify(fetch_articles('https://openai.com/blog'))

@app.route('/article/<int:number>')
def article(number):
    articles = fetch_articles('https://openai.com/blog')
    if 0 <= number < len(articles):
        return jsonify(articles[number])
    return jsonify({'error': 'Article not found'}), 404

@app.route('/ml/')
@app.route('/ml/<int:number>')
def ml(number=None):
    articles = fetch_articles('https://openai.com/blog')
    if number is not None:
        if 0 <= number < len(articles):
            article = articles[number]
            sentiment = analyze_sentiment(article['title'])
            return jsonify({'number': number, 'sentiment': sentiment})
        return jsonify({'error': 'Article not found'}), 404
    else:
        sentiments = {article['title']: analyze_sentiment(article['title']) for article in articles}
        return jsonify({'all_articles_sentiment': sentiments})

@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
