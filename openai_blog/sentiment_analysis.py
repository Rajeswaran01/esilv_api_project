import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download the VADER lexicon
nltk.download('vader_lexicon')

def analyze_sentiment(text):
    """
    Analyzes the sentiment of the provided text.

    :param text: The text to analyze sentiment of.
    :return: A dictionary containing the sentiment scores.
    """
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(text)
