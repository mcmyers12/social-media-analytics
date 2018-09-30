__author__ = 'piorkja1'

import nltk
from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import SnowballStemmer
from io import open
import pprint

def get_tokens():
	with open('acro-yoga-reddit-comments.txt') as stem:
		tokens = nltk.word_tokenize(stem.read())
	return tokens

def do_stemming(filtered):
	stemmed = []
	for f in filtered:
		#stemmed.append(PorterStemmer().stem(f))
		#stemmed.append(LancasterStemmer().stem(f))
		stemmed.append(SnowballStemmer('english').stem(f))
	return stemmed

if __name__ == "__main__":

	tokens = get_tokens()

	stemmed_tokens = do_stemming(tokens)

	result = dict(zip(tokens, stemmed_tokens))
	print("{tokens:stemmed} = ",  result)

	file = open("stemmingoutput.txt", "w", encoding="utf-8")
	file.write(unicode("stemming output " + '\n'))
	count = 0
	for key in result:
		file.write(unicode(key + ' --> ' + result[key] + '\n'))
		count += 1
		if count == 200:
			exit()
