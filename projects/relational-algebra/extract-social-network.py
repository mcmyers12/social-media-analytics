'''Extract a structured data set from a social media of your choice. For example, you might have
user_ID associated with forum_ID. Use relational algebra to extract a social network (or forum
network) from your structured data. Create a visualization of your extracted network. What
observations do you have in regards to the network structure of your data?

Create a network using authors of comments from subreddits:
    r/AcroYoga, r/Yoga, and r/Dance'''


import praw
import pprint as pp
from igraph import *


def getCommentAuthors(r, authors, subreddits, authorCount):
    for subredditName in subreddits:
        subreddit = r.subreddit(subredditName)
        for post in subreddit.comments(limit=authorCount):
            author = post.author.name
            if author in authors:
                if subreddit.display_name not in authors[author]['subreddits']:
                    authors[author]['subreddits'].append(subreddit.display_name)
            else:
                authors[author] = {'subreddits': [subreddit.display_name]}


def createGraph():
    g = Graph()


def createAdjacencyMatrix(g, file):
    file.write('Adjacency Matrix: \n')
    g.write_adjacency(file)


def main():
    r = praw.Reddit(client_id='1RmB7ChqHgjuZw', client_secret='xl04Tf2edeM6k_0hmnQrWFdmvrs', user_agent='me')
    authors = {}

    authorCount = 10
    subreddits = ['AcroYoga', 'Yoga', 'Dance']
    getCommentAuthors(r, authors, subreddits, authorCount)


    #pp.pprint(vars(subreddit))
    pp.pprint(authors)

    for author in authors:
        if len(authors[author]['subreddits']) > 1:
            print author
            pp.pprint(authors[author])

main()
