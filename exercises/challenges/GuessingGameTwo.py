import sys
import random
import requests
from bs4 import BeautifulSoup

def get_input(help_text='choose > or < or =: '):
    return str(raw_input(help_text))

def binary_search(List):
    count = 0
    
    while len(List) >= 1:    
        if len(List) % 2 == 0:
            mid_index = len(List)/2-1
        else:
            mid_index = (len(List)+1)/2-1
    
        print 'Your Guess number is %s' %(List[mid_index])
        check = get_input('Choose > or < or =: ')
        count+=1

        if check == '>':
            if len(List) == 2:
                print 'Your Guess number is %s' %(List[mid_index-1])
                print 'It took %s chances to guess' %(count)
                break
            else:
                List = List[:mid_index]
        elif check == '<':
            if len(List) == 2:
                print 'Your Guess number is %s' %(List[mid_index+1])
                print 'It took %s chances to guess' %(count)
                break
            else:
                List = List[mid_index:]
        elif check == '=':
            print 'Thanks for playing the Guess Game'
            print 'It took %s chances to guess' %(count)
            break
        
def main():
    print '***************** Welcome to Guess Game!!! ****************'
    List = random.sample(range(0,101),101)
    print "*** Imagine a number between 0 and 100, Dont tell any one ***"
    binary_search(sorted(List))

if __name__ == '__main__':
    main()