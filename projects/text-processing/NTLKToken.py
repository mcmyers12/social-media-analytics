_author__ = 'piorkja1'

import nltk
from io import open


stem = open('acro-yoga-reddit-comments.txt','r')
wtokens = nltk.word_tokenize(stem.read())
stem = open('acro-yoga-reddit-comments.txt','r')
ctokens = nltk.casual_tokenize(stem.read())
stem = open('acro-yoga-reddit-comments.txt','r')
stokens = nltk.sent_tokenize(stem.read())



print("word tokens = ",  wtokens)
print("casual tokens = ",  ctokens)
print("sentence tokens = ",  stokens)

file = open("tokenoutput.txt", "w", encoding="utf-8")
file.write(unicode("word tokens " + '\n'))
count = 0
for item in wtokens:
  file.write(unicode("%s\n" % item))
  count += 1
  if count > 100:
      break

count = 0
file.write(unicode("\n\ncasual tokens " + '\n'))
for item in ctokens:
  file.write(unicode("%s\n" % item))
  count += 1
  if count > 100:
      break

count = 0
file.write(unicode("\n\nsentence tokens " + '\n'))
for item in stokens:
  file.write(unicode("%s\n" % item))
  count += 1
  if count > 100:
      break
