import sys
import random
import requests
from bs4 import BeautifulSoup

def get_input(help_text='Enter number to draw a board: '):
    return int(input(help_text))

def draw_game_board(num):
    print '\n'
    header = ''
    body_line1 = ''
    i = num
    j = num
    
    #header prep
    while i > 0:
        header = header + ' ---'
        i -=1
    #First Line
    print header
    
    #body prep
    while j > -1:
        body_line1 = body_line1 + '|' + '   '
        j -=1
    
    #Looping to print
    while num > 0:
        print body_line1 + '\n' + header
        num -=1
    print '\n'
def main():
    print 'Welcome to Draw a Game Board!!!'
    num = get_input('Enter number to draw num*num board: ')
    draw_game_board(num)
    #another solution
    #print(" ---" * num)

if __name__ == '__main__':
    main()