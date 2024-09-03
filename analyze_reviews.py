import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import re

def clean_text(text):
    # Remove non-alphabetical characters and convert to lowercase
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = text.lower()
    return text

def analyze_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

def visualize_wordcloud(text):
    try:
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()
    except ValueError as e:
        print(f"Error generating word cloud: {e}")

if __name__ == "__main__":
    df = pd.read_csv('amazon_reviews.csv')

    # Clean the review content before processing
    df['Content'] = df['Content'].apply(clean_text)

    # Sentiment Analysis
    df['Sentiment'] = df['Content'].apply(analyze_sentiment)

    # Summary Statistics
    sentiment_counts = df['Sentiment'].value_counts()
    print(sentiment_counts)

    # Word Cloud Visualization
    all_reviews = ' '.join(df['Content'].tolist())
    visualize_wordcloud(all_reviews)

    # Plot Sentiment Distribution
    try:
        df['Sentiment'].value_counts().plot(kind='bar')
        plt.title('Sentiment Distribution')
        plt.xlabel('Sentiment')
        plt.ylabel('Frequency')
        plt.show()
    except Exception as e:
        print(f"Error plotting sentiment distribution: {e}")
