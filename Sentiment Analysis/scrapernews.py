import requests
import textblob
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from textblob import TextBlob
from newspaper import Article

df = pd.DataFrame(columns= ['search_term', 'polarity', 'subjectivity', 'date_posted', 'keywords', 'article_url'])

search_term = input("Enter a stock to search sentiment on: ")
headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
}

params = {
    "q": (search_term + ' stock'),
    "hl": "en",
    "gl": "us",
    "tbm": "nws",
    "tbs": "qdr:d"
}

html = requests.get('https://www.google.com/search', headers=headers, params=params)
soup = BeautifulSoup(html.text, 'lxml')

for result in soup.select('.WlydOe'):
    title = result.select_one('.nDgy9d').text
    link = result['href']
       #this uses the newspaper library to build an article object of the article it just read
    try:
        article = Article(link)
        article.download()
        article.parse()
        article.nlp()
        #here we start the sentiment analysis
        blob = TextBlob(article.text)
        blob2 = TextBlob(article.summary)
        print('Title: ' + title, link, sep='\n')
        print(article.summary)
        print('whole article sentiment')
        print(blob.sentiment)
        print('Polarity: ', blob.polarity)
        print('Subjectivity: ', blob.subjectivity)
        print('summary of article sentiment')
        #print(blob2.sentiment)
        print('Polarity: ', blob2.polarity)
        print('Subjectivity: ', blob2.subjectivity)
        print('')
        #update pandas library
        df.loc[len(df.index)] = [search_term, blob.polarity, blob.subjectivity, article.publish_date, article.keywords, link]
    except:
        print('error loading website')

print(df)

df.to_csv(search_term+'__.csv', date_format ='%Y-%m-%d', sep=',', encoding='utf-8')

