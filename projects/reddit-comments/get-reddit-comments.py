'''Select a  Reddit page and download comments from each using a python script.'''

import praw

r = praw.Reddit(client_id = '1RmB7ChqHgjuZw', client_secret='xl04Tf2edeM6k_0hmnQrWFdmvrs', user_agent='me')
file = open('acro-yoga-reddit-comments.txt', 'w')

for post in r.subreddit('AcroYoga').comments(limit=200):
    print post.body
    comment = post.body.encode('utf-8')
    file.write(comment + '\n\n')

file.close()