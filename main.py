with open("miracle_in_the_andes.txt." , 'r', encoding='utf-8') as file:
    book=file.read()

import re
pattern = re.compile("[a-zA-Z]+")
findings=re.findall(pattern,book.lower())

dictionary={}
for item in findings:
    if item in dictionary.keys():
        dictionary[item] = dictionary[item]+1
    else:
        dictionary[item] = 1

newlist = [(item,key) for key,item in dictionary.items()]
newlist = sorted(newlist, reverse=True)

#Most used NON-STOP words in a book?
from nltk.corpus import stopwords
english_stopwords = stopwords.words("english")
# print(english_stopwords)

filtered_words=[]
for value,word in newlist:
    if word not in english_stopwords:
        filtered_words.append((value,word))
print(filtered_words[:10])

# SENTIMENT ANALYSIS - what is the most positive and negative chapters in book?
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
# nltk.download('vader_lexicon')
analyzer = SentimentIntensityAnalyzer()

import re
pattern = re.compile("Chapter [0-9]+")
chapters = re.split(pattern, book)[1:]

scores=[]
for chapter in chapters:
    print(analyzer.polarity_scores(chapter))





