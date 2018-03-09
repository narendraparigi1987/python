import sys
import random
import requests
from bs4 import BeautifulSoup
import time
import json

birthdays = {}
with open(r'C:\Python27\birthday.json','r') as f:
    birthdays = json.load(f)

def get_input(help_text='Enter your option: '):
    return str(raw_input(help_text))

def add_entry():
    name = get_input('Enter name of whom Birthday you wish to add: ')
    date = get_input('Enter birth date of %s: '%(name))
    birthdays[name] = date
    open_file = open(r'C:\Python27\birthday.json','w')
    json.dump(birthdays,open_file)
    open_file.close()

def find_entry():
    key = get_input("Who's birthday do you want to look up? ")
    print 'Birthday of {} is {} '.format(key,birthdays[key])

def list_entries():
    print 'Welcome to the birthday dictionary. We know the birthdays of'
    time.sleep(1)
    for key in birthdays.keys():
        print key
        time.sleep(0.7)

def main():
    print 'Welcome to Birthday Json program'
    print '''It will take below options
    Quit
    Add
    Find
    List
    '''
    what_next=get_input('Enter your option: ')
    if what_next == 'Quit':
        print 'Good bye'
        exit(0)
    elif what_next == 'Add':
        add_entry()
    elif what_next == 'Find':
        find_entry()
    elif what_next == 'List':
        list_entries()

if __name__ == '__main__':
    main()