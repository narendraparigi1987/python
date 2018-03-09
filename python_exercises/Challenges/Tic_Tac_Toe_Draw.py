import sys
import random
import requests
from bs4 import BeautifulSoup

def get_input(help_text='Enter size of borad: '):
    return raw_input(help_text)

def draw_board(size):
    i=size
    j=i+1
    print (' ---' * size)
    while i > 0:
        print ('|   ' * j)
        print (' ---' * size)
        i-=1

def update_list(choice_list,list,iteration,player):
    if (list[choice_list[0]][choice_list[1]] == 'x') or (list[choice_list[0]][choice_list[1]] == 'o'):
        print '\nAlready chosen!!!, pick another choice'
        return list, iteration+1
    elif player == 1:
        list[choice_list[0]][choice_list[1]] = 'x'
    elif player == 2:
        list[choice_list[0]][choice_list[1]] = 'o'
    return list, iteration

def transpose(game):
    return [[row[i] for row in game] for i in range(len(game))]

def check_winner(size,game,game_transpose):
    player1 = ['x' for i in range(len(game))]
    player2 = ['o' for i in range(len(game))]
    i = size-1
    while i >=0:
        if game[i] == player1 or game_transpose[i] == player1:
            return 1
            break
        elif game[i] == player2 or game_transpose[i] == player2:
            return 2
            break
        i-=1
    if [game[i][i] for i in range(len(game))] == player1 or [game[i][~i] for i in range(len(game))] == player1:
        return 1
    elif [game[i][i] for i in range(len(game))] == player2 or [game[i][~i] for i in range(len(game))] == player2:
        return 2

def play_game(size):
    iteration = size*size
    list = [[0 for i in range(0,size)] for i in range(0,size)]
    player = ''
    while iteration > 0:
        if size % 2 == 0:
            if iteration % 2 == 0:
                choice = get_input('\nplayer1: enter your choice: ')
                player = 1
            else:
                choice = get_input('\nplayer2: enter your choice: ')
                player = 2
        else:
            if iteration % 2 == 0:
                choice = get_input('\nplayer2: enter your choice: ')
                player = 2
            else:
                choice = get_input('\nplayer1: enter your choice: ')
                player = 1
        choice_list = choice.strip().split(',')
        choice_list = [int(i)-1 for i in choice_list]
        if choice_list[0] >= size or choice_list[1] >=size:
            print '\nInvalid choice, enter correct option based on size of matrix'
        else:
            (list,iteration) = update_list(choice_list,list,iteration,player)
            iteration-=1
            print '\n'
            game = list
            game_transpose = transpose(game)
            result = check_winner(size,game,game_transpose)
            if result == 1:
                print game
                print '\nPlayer1 won'
                break
            elif result == 2:
                print game
                print '\nPlayer2 won'
                break
            else:
                print game
                continue
    print '\nGame is completed !!!!'

def main():
    print '\nWelcome to Tic Tac Toe Game!!!'
    print '\nEnter choice in rowindex,columnidex Index starts from 1 instead 0'
    size = int(get_input('\nEnter size of board: '))
    draw_board(size)
    play_game(size)

if __name__ == '__main__':
    main()