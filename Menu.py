import Streams
from termcolor import colored, cprint

def football():
    input_color = colored("Please choose from the following options:\nStats 'S', Highlights 'H', Live Streams 'L', Exit 'E'\n",'red',attrs=['bold'])
    choose_menu = raw_input(input_color)

    if choose_menu == 'H' or choose_menu == 'h':
        Streams.highlights()
        Restart_menu()

    if choose_menu == 'l' or choose_menu == 'L':
        Streams.footballLinks()
        Restart_menu()

def Restart_menu():
    football()

Streams.login()
football()