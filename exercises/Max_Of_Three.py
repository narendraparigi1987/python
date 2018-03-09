import sys
import random
import requests
from bs4 import BeautifulSoup

def get_input(help_text='enter a number: '):
    return str(raw_input(help_text))

def find_max(num1,num2,num3):
    big = num1
    if num3 >= big:
        big = num3
        if num2 > num3:
            big = num2
    elif num2 >= big:
        big = num2

    return big

def main():
    num1 = get_input('enter a value for input1: ')
    num2 = get_input('enter a value for input2: ')
    num3 = get_input('enter a value for input3: ')
    result = find_max(num1,num2,num3)
    print 'Maximum number is %s' %(result)

if __name__ == '__main__':
    main()