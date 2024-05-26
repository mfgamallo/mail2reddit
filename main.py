#
# main.py
# Email to Reddit forwarder - Proof of Concept
# Gamallo 2024
#

from mail import get_posts, send_to_trash
from reddit import send_post

print("===========\nStarting...\n===========")

posts = get_posts()

if (len(posts)):
    for key, post in posts.items():
        send_post(post)
        send_to_trash(key)

print("===========\n...finished\n===========")
