import sys
import random
import requests
from bs4 import BeautifulSoup
import time

def get_input(help_text="Who's birthday do you want to look up?"):
    return str(raw_input(help_text))

def main():
    birthdays = {
        'Albert Einstein': '03/14/1879',
        'Benjamin Franklin': '01/17/1706',
        'Ada Lovelace': '12/10/1815',
        'Donald Trump': '06/14/1946',
        'Rowan Atkinson': '01/6/1955'
        }
    print 'Welcome to the birthday dictionary. We know the birthdays of:'
    time.sleep(1)
    for name in birthdays.keys():
        print name
        time.sleep(0.7)
    key = get_input("Who's birthday do you want to look up? ")
    print "Benjamin Franklin's birthday is {}" .format(birthdays[key])

if __name__ == '__main__':
    main()