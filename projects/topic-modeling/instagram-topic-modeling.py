import json
import gensim
import urllib2
import pyLDAvis.gensim
from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize
from gensim import corpora, models, similarities


stop_words = set(stopwords.words('english'))
stop_words.update(['.',  ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}', '#', '@', '##########', '-', ')-', '-------------------------------------------------', '!!']) # remove if you need punctuation

def get_instagram_caption_terms(hashtag):
    search_url = 'https://www.instagram.com/explore/tags/' + hashtag + '/?__a=1'
    contents = urllib2.urlopen(search_url).read()
    results = json.loads(contents)
    edges = results['graphql']['hashtag']['edge_hashtag_to_media']['edges']
    for edge in edges:
        captions = edge['node']['edge_media_to_caption']['edges']
        for caption in captions:
            text = caption['node']['text']
            words = [i.lower() for i in wordpunct_tokenize(text.encode('ascii', 'ignore')) if i.lower() not in stop_words]
            all_tokens = ' '.join(words)
    texts = words
    # remove words that appear only once
    tokens_once = set(words for words in set(all_tokens) if all_tokens.count(words) == 1)
    texts = [[words for words in texts if words not in tokens_once]
             for words in all_tokens]
    return texts
    
texts = get_instagram_caption_terms('acroyoga') +         get_instagram_caption_terms('pointe') +         get_instagram_caption_terms('watercolor')

#Setup gensim dictionary
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]

lda = gensim.models.LdaModel(corpus, id2word=dictionary, alpha='auto', num_topics=10)
for i in lda.show_topics():
    print (i)

topic_vis = pyLDAvis.gensim.prepare(lda, corpus, dictionary)

pyLDAvis.display(topic_vis)

