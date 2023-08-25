# nltk is imported because other two library textblob and newspaper is based upon it
import nltk

# Textblob library is being used for actual sentimental analysis
from textblob import TextBlob

# actual library name for newspaper is newspaper3k which we are going to get newspaper article into our script for sentimental analysis
from newspaper import Article

nltk.download('punkt')

# specifying the url of the article
url = 'https://www.ndtv.com/india-news/flood-washes-away-uttarakhand-bridge-contact-lost-with-border-villages-4196545'

# Converting the content of the url to an article object of newspaper library
article = Article(url)

article.download()      # to get the article into the script
article.parse()     # to make the article more readable or get all the HTML out of the article
article.nlp()       # preparing the article for natural language processing

text = article.summary      # from summary, we can focus on the main content of the article
print(text)


# we are going to pick the summary(dataset) of the article for sentiment analysis

# creating the textblob object
blob = TextBlob(text)

# checking the sentiment of the blob in terms of polarity which is going to give us result from -1 to 1
sentiment = blob.sentiment.polarity     # -1 to 1

print('sentimental analysis of the given article is ', sentiment)
