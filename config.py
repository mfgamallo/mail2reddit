#
# config.py
# Gather configuration for E2R
# Gamallo 2024
#

import os

source_mailbox_name = os.environ['m2r_mailbox']
mail_subject_regex_filter = os.environ['m2r_subject_regex']
mail_subdir_filter = os.environ['m2r_subdir']
mail_flag_filter = os.environ['m2r_flag']
subreddit_name = os.environ['m2r_subreddit']
