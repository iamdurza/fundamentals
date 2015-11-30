#!/usr/bin/env python3

import skilstak.colors as c
import time

   

def print_plain(message):
    '''Clears the screen & says 'Hello World'.'''
    print(c.clear + c.rc() + message + c.reset)

def print_multi(message):
    '''Print hello world to the console with each charecter in random colors.'''
    
    while True:
            print(c.clear + c.multi(message))
            time.sleep(0.5)
    
def print_colored(message):
    '''Prints like nyan.'''
    print(c.clear)
    while True:
        print(c.rc() + message + c.x, end=" ")
def parse_args():
    from sys import argv
    
    name = "world"
    option = ""

    if len(argv) > 2:
        option = argv[1]
        name = argv[2]
    elif len(argv) == 2:
        if argv[1].startswith("-"):
                option = argv[1]
        else:
            name = argv[1];
    return name, option 


        
