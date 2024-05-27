#
# main.py
# Email to Reddit forwarder - Proof of Concept
# Gamallo 2024
#

from censor import censor_posts
from mail import get_posts, send_to_trash
from reddit import send_post

print("===========\nStarting...\n===========")

posts = get_posts()

censored_posts = censor_posts(posts)

if (len(censored_posts)):
    for key, post in censored_posts.items():
        send_post(post)
        send_to_trash(key)

print("===========\n...finished\n===========")
