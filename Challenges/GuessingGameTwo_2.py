import sys
import random
import requests
from bs4 import BeautifulSoup

def guess():
    i=0
    j=100
    m=50
    count = 1
    
    print '''
    0 means too low
    1 means its your guess
    2 means too high
    '''
    condition = input('is your guess numer %s? ' %(m))
    
    while condition !=1:
        count+=1
        if condition == 0:
            i = m+1
        elif condition == 2:
            j = m-1
        m = (i+j)/2
        condition = input('is your guess numer %s? ' %(m))
    print 'Number of guesses %s' %(count)


def main():
    print 'Welcome to Guess Game!!!'
    guess()

if __name__ == '__main__':
    main()