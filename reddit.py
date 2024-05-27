#
# reddit.py
# Deal with reddit for M2R
# Gamallo 2024
#

import praw

from config import subreddit_name

def send_post(post):
    reddit = praw.Reddit()
    subreddit = reddit.subreddit(subreddit_name)
    print("Publishing post with title " + post['title'] + " to subreddit" + subreddit_name)
    subreddit.submit(title=post['title'], selftext=post['text'])
    print("Published post with title " + post['title'] + " to subreddit" + subreddit_name)
