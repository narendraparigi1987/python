import sys
import random
import requests
from bs4 import BeautifulSoup
import time
import json
from collections import Counter
from bokeh.plotting import figure, show, output_file

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

def List_Months():
    Months_List = []
    Months_Dic = {
        '01':'Jan',
        '02':'Feb',
        '03':'Mar',
        '04':'Apr',
        '05':'May',
        '06':'Jun',
        '07':'Jul',
        '08':'Aug',
        '09':'sep',
        '10':'Oct',
        '11':'Nov',
        '12':'Dec',
    }
    for value in birthdays.values():
        check_value = value[2] + value[3]
        for key, value in Months_Dic.items():
            if check_value == key:
                Months_List.append(value)
    return Months_List,Months_Dic

def histogram():
    (Months_List,Months_Dic) = List_Months()
    x_categories = Months_Dic.values()
    Months_Dic = Counter(Months_List)
    x = Months_Dic.keys()
    y = Months_Dic.values()
    output_file("C:\\Python27\\bokeh.html")
    p = figure(x_range = x_categories)
    p.vbar(x=x, top=y, width=0.5)
    show(p)


def main():
    print 'Welcome to Birthday Json program'
    print '''It will take below options
    Quit
    Add
    Find
    List
    List_Months
    histogram
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
    elif what_next == 'List_Months':
        (Months_List,Months_Dic) = List_Months()
        print 'Number of birthdays is each month are {}'.format(Counter(Months_List))
    elif what_next == 'histogram':
        histogram()

if __name__ == '__main__':
    main()