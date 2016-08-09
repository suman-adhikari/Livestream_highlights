# coding=utf-8
# re:regular expression
#  The sys module provides information about constants, functions and methods of the Python interpreter.
#  Python reddit API Wrapper,python package that allows for simple access to reddit’s API

import praw
import re
from termcolor import colored,cprint
import sys
import webbrowser

user_agent = ("Link Getter");
# crate instance of Redit
r = praw.Reddit(user_agent=user_agent);

def login():
    r.login('suman_ad','connectifyRED',disable_warnings=True)

    print_login=colored('Logging ... \n','yellow');
    print(print_login);


def highlights():
    subredit  = r.get_subreddit("footballhighlights")

    # get first 15 submission from hot section
    for submission in subredit.get_hot(limit=15):
        print("Highlights: ", submission.title)


    print_input_choose = colored("Which Highlight you'd like to watch? \n");
    highlight = raw_input(print_input_choose)

    cprint ("Double Click Link to open on browser",'red')

    for submission in subredit.get_hot(limit=80):
        if(re.search(highlight,submission.title,re.IGNORECASE)):
            print("\n Title: " , submission.title)
            print(submission.selftext)


def footballLinks():
    subredit_link = r.get_subreddit("soccerstreams")

    for submission in subredit_link.get_hot(limit=15):
      print("Live Links: ", submission.title)

    print_input_link = colored("Which Game would you like to stream? \n")
    live_stream = raw_input(print_input_link)

    cprint ("Double Click Link to open on browser",'green')

    for submission in subredit_link.get_hot(limit=15):
        if(re.search(live_stream,submission.title,re.IGNORECASE)):
            print("\n Title ", submission.title)
            print("\n Link: ", submission.url)



