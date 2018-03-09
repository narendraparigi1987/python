import sys
import random
import requests
from bs4 import BeautifulSoup

def transpose(game):
    return [[row[i] for row in game] for i in range(len(game))]

def find_winner(game,game_transpose):
    
    i = len(game)-1
    print '''
    0 is for no player
    1 is for player 1
    2 is for player 2
    '''
    winner1 = [1 for i in range(len(game))]
    winner2 = [2 for i in range(len(game))]
    #checking for columns and rows
    while i >=0:
        if game[i] == winner1 or game_transpose[i] == winner1:
            return 'Winner is 1'
            break
        elif game[i] == winner2 or game_transpose[i] == winner2:
            return 'winner is 2'
            break
        i-=1
    #checking for diagonals
    if  [game[i][i] for i in range(len(game))] == winner1 or [game[i][~i] for i in range(len(game))] == winner1:
        return 'winner is 1'
    elif [game[i][i] for i in range(len(game))] == winner2 or [game[i][~i] for i in range(len(game))] == winner2:
        return 'winner is 2'
    else:
        return 'no winner'

def main():
    print 'Welcome to the Tic Tac Toe game !!!'
    game = [[1, 2, 0,2],[2, 1, 0,2],[2, 1, 0,2],[2, 1, 0,2]]
    game_transpose = transpose(game)
    result = find_winner(game,game_transpose)
    print result

if __name__ == '__main__':
    main()