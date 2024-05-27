#
# censor.py
# Apply censoring rules so unadequate messages don't pass through
# Gamallo 2024
#

import re

from config import censoring_regex

def censor_posts(posts):

    censored_posts = {}
    
    for key, post in posts.items():
        if(not re.search(censoring_regex, post['text'])):
            censored_posts[key] = post
        else:
            print("Discarded message with key " + key + " because it matches regex " + censoring_regex)
        
    return censored_posts
