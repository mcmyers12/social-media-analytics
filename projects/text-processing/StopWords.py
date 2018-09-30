__author__ = 'piorkja1'

import nltk

f = open('reddit.txt','r')
data = f.read()


# tokenize the data

#w = nltk.word_tokenize(data)

#print (w)

# Remove stopwords
from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize

#file = open("temp.txt", "w")  # scratch file

stop_words = set(stopwords.words('english'))
stop_words.update(['.',  ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']',"intro",'{', '}']) # remove it if you need punctuation
#for data in documents:
words = [i.lower() for i in wordpunct_tokenize(data) if i.lower() not in stop_words]
#print (words)

text = ' '.join(words)

print ("clean text =", text)
