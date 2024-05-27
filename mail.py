#
# mail.py
# Deal with mailboxes for E2R
# Gamallo 2024
#

import mailbox
import re

from config import source_mailbox_name, mail_subject_regex_filter, mail_subdir_filter, mail_flag_filter


def can_be_sent(maildir, key):
    message = maildir.get_message(key)
    return (message.get_subdir()==mail_subdir_filter and
            re.match(mail_subject_regex_filter, message['subject']) and
            mail_flag_filter not in message.get_flags())


def get_body(message):
    if(message.is_multipart()):
        return get_body(message.get_payload()[0])
    else:
        return message.get_payload(decode=True).__str__()

    
def get_post(body):
    regex = "^On .*wrote:"
    for line in body.splitlines():
        stripped = line.strip()
        if(len(stripped) and stripped[0].isalnum()) and not re.match(regex, stripped):
            return {'title': line, 'text': body}
    return {'title': "", 'text': body}


def get_posts():

    posts = {}
    
    print("Looking into mailbox " + source_mailbox_name + " for messages that:\n" +
      "* Are in subdir " + mail_subdir_filter + "\n" +
      "* Have a subject that matches " + mail_subject_regex_filter + "\n" +
      "* Do NOT have flag " + mail_flag_filter)

    maildir = mailbox.Maildir(source_mailbox_name, create=False)

    keys_to_send = [key for key in maildir.keys() if can_be_sent(maildir, key)]

    if (not len(keys_to_send)):
        print("No messages found to send")
    else:
        print("Found the following messages be sent:")
        for key in keys_to_send: print(key)

        for key in keys_to_send:
            print("Readying message " + key)
            message = maildir.get_message(key)
            mail_body = get_body(message)
            post = get_post(mail_body)
            print("Using title: " + post['title'])
            posts[key] = post

    return posts


def send_to_trash(key):
    print("Sending to trash email message with key " + key)
    maildir = mailbox.Maildir(source_mailbox_name, create=False)
    message = maildir.get_message(key)
    message.add_flag(mail_flag_filter)
    maildir.__setitem__(key, message)
