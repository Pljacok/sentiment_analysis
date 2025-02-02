import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")
sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    scores = sia.polarity_scores(text)
    if scores["compound"] > 0.05:
        return "Позитивний 🙂"
    elif scores["compound"] < -0.05:
        return "Негативний 😠"
    else:
        return "Нейтральний 😐"

if __name__ == "__main__":
    text = input("Введіть коментар: ")
    print("Настрій коментаря:", analyze_sentiment(text))
