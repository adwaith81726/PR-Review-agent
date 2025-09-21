from ntscraper import Nitter
from textblob import TextBlob
import pandas as pd

# Initialize scraper
scraper = Nitter(log_level=1, skip_instance_check=False)

# Get tweets containing the hashtag "kanye"
github_hash_tweets = scraper.get_tweets("samayraina", mode='term', number=10)

# Extract tweet text
tweet_texts = [tweet["text"] for tweet in github_hash_tweets["tweets"]]

# Sentiment analysis function
def classify_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0:
        return "Positive", 100
    elif polarity < 0:
        return "Negative", 0
    else:
        return "Neutral", 50

# Classify sentiment for each tweet and store values
sentiments = []
sentiment_values = []

for tweet in tweet_texts:
    sentiment, value = classify_sentiment(tweet)
    sentiments.append(sentiment)
    sentiment_values.append(value)

# Calculate sentiment score (starting at 50)
if sentiment_values:
    sentiment_score = 50 + (sum(sentiment_values) / len(sentiment_values) - 50)
else:
    sentiment_score = 50

# Save to Excel
df = pd.DataFrame({"Tweet": tweet_texts, "Sentiment": sentiments})
df.to_excel("tweets_sentiment.xlsx", index=False)

print(f"Sentiment analysis saved to tweets_sentiment.xlsx")
print(f"Sentiment Score: {sentiment_score:.2f}")

