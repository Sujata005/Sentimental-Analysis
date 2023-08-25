from textblob import TextBlob

with open('text.txt', 'r') as f:
    text = f.read()

blob = TextBlob(text)
sentiment = blob.sentiment.polarity
if sentiment < 0:
    print('Text is negative')
elif sentiment > 0:
    print('Text is positive')
elif sentiment == 0:
    print('Text is neutral')
print(sentiment)
