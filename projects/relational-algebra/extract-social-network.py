'''Extract a structured data set from a social media of your choice. For example, you might have
user_ID associated with forum_ID. Use relational algebra to extract a social network (or forum
network) from your structured data. Create a visualization of your extracted network. What
observations do you have in regards to the network structure of your data?

Create a network using authors of comments from subreddits'''


import praw
from igraph import *


def getCommentAuthors(r, authors, subreddits, authorCount):
    for subredditName in subreddits:
        subreddit = r.subreddit(subredditName)
        for post in subreddit.comments(limit=authorCount):
            if post.author and post.author.name:
                author = post.author.name
                if author in authors:
                    if subreddit.display_name not in authors[author]['subreddits']:
                        authors[author]['subreddits'].append(subreddit.display_name)
                else:
                    authors[author] = {'subreddits': [subreddit.display_name]}


def formatGraph(g, authors, subreddits):
    authorList = list(authors.keys())
    labels = subreddits + ['' for x in range(len(authorList))]
    g.vs['label'] = labels
    colors = ['teal' for x in range(len(subreddits))] + ['purple' for x in range(len(authors.keys()))]
    g.vs['color'] = colors
    addEdges(g, authorList, authors, subreddits)


def addEdges(g, authorList, authors, subreddits):
    for i in range(len(authorList)):
        author = authorList[i]
        authorSubreddits = authors[author]['subreddits']
        vertexNumber = i + len(subreddits)
        subredditNumbers = [subreddits.index(s) for s in authorSubreddits]
        for subredditNumber in subredditNumbers:
            g.add_edge(vertexNumber, subredditNumber)


def createGraph(authors, subreddits):
    g = Graph()
    g.add_vertices(len(authors) + len(subreddits))
    formatGraph(g, authors, subreddits)
    plot(g)


def main():
    r = praw.Reddit(client_id='1RmB7ChqHgjuZw', client_secret='xl04Tf2edeM6k_0hmnQrWFdmvrs', user_agent='me')
    authors = {}

    authorCount = 50
    subreddits = ['dance', 'ballet', 'dancemoms', 'dancingwiththestars', 'worldofdance', 'thebachelor']
    getCommentAuthors(r, authors, subreddits, authorCount)

    createGraph(authors, subreddits)


main()
