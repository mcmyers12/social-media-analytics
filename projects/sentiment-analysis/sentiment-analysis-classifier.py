import nltk
from pprint import pprint as pp
from enum import Enum

'''Sentiment analysis classifier using the Sentiment 140 corpus and NLTK.
   Tested using content from Reddit. 
   Data from http://help.sentiment140.com/for-students
   Code adapted from https://www.laurentluce.com/posts/twitter-sentiment-analysis-using-python-and-nltk/'''

'''Limitations: doesn't remove stop words well, improve filtering'''



class Sentiment(Enum):
    negative = 0
    neutral = 2
    positive = 4


def get_tweets(csvFile):
    tweets = []
    with open(csvFile, 'r') as f:
        for line in f:
            columns = line.split(',')
            sentiment = Sentiment(int(columns[0].replace('"','')))
            tweet = columns[5]
            filteredTweet = [e.lower().replace('"','') for e in tweet.split() if len(e) >= 3]
            tweets.append((filteredTweet, sentiment.name))

    return tweets


def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
      all_words.extend(words)
    return all_words


def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()

    return word_features


training_tweets = get_tweets('training-and-test-data/training.1600000.processed.noemoticon.csv')
test_tweets = get_tweets('training-and-test-data/testdata.manual.2009.06.14.csv')
word_features = get_word_features(get_words_in_tweets(training_tweets))


def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features


def build_sentiment_classifier():
    training_set = nltk.classify.apply_features(extract_features, training_tweets)
    classifier = nltk.NaiveBayesClassifier.train(training_set)
    print 'classifier accuracy on test set:'
    test_set = nltk.classify.apply_features(extract_features, test_tweets)
    print '\t' + str(nltk.classify.accuracy(classifier, test_set)) + '\n\n'
    reddit_sentiment_classification(classifier)


def reddit_sentiment_classification(classifier):
    print 'example classifications of reddit comments: '
    with open('training-and-test-data/acro-yoga-reddit-comments.txt', 'r') as f:
        comments = [next(f) for x in xrange(15)]
        for comment in comments:
            print '\tcomment: '
            print '\t\t' + comment.replace('\n','')
            print '\tsentiment: '
            print '\t\t' + classifier.classify(extract_features(comment.split()))
            print


build_sentiment_classifier()