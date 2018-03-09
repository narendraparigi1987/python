import sys
import random
import requests
from bs4 import BeautifulSoup

def create_list():
    list = []
    open_file  = open(r'C:\Python27\sowpods.txt','r')
    #for line in open_file.readlines():
    #    list.append(line.strip())
    while True:
        line = open_file.readline()
        if line:
            list.append(line.strip())
        else:
            break
    return list

def select_random_word(list):
    return random.choice(list)

def get_input(help_text='\nEnter a letter: '):
    return str(raw_input(help_text))

def main():
    print '\nWelcome to Hangman !!!'
    list = create_list()
    word = random.choice(list)
    letter_list = []
    his_letter_list = []
    guess_dic = {}
    for i,word in enumerate(word):
        letter_list.append(word)
        guess_dic[i] = '_'
    status = 0
    count = 0
    print letter_list
    print guess_dic.values()
    while status != 1:
        letter = get_input('\nEnter a letter: ')
        his_letter_list.append(letter)
        if letter in letter_list:
            for i in range(len(his_letter_list)):
                letter = his_letter_list[i]
                for j, word in enumerate(letter_list):
                    if letter == word:
                        guess_dic[j] = word
            print guess_dic.values()
        else:
            print 'Incorrect answer!!!'
        if letter_list == guess_dic.values():
            print 'Congrats, guess is correct now, number guesses %s' %(count)
            status = 1
        count+=1

if __name__ == '__main__':
    main()