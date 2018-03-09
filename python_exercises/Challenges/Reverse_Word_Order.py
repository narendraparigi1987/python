import sys
import random

def get_input(help_text='enter string: '):
    return str(raw_input(help_text))

def get_list(text_string):
    return text_string.split(' ')

def get_string(list_string):
    return ' '.join(list_string[::-1])

def main():
    print 'welcome'
    text_string = get_input('enter string for reverse word order: ')
    list_string = get_list(text_string)
    result_string = get_string(list_string)
    print result_string

if __name__ == '__main__':
    main()