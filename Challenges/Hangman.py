import sys
import random
import requests
from bs4 import BeautifulSoup

def create_words_list():
    words = []
    open_file = open(r'C:\Python27\sowpods.txt','r')
    while True:
        line = open_file.readline().strip()
        if line:
            words.append(line)
        else:
            break
    return words

def random_choice(words):
    letter_list = []
    letter_dic = {}
    word = random.choice(words)
    for i,letter in enumerate(word):
        letter_list.append(letter)
        letter_dic[i] = '_'
    return letter_list, letter_dic

def get_input(help_text='\nEnter your letter: '):
    return str(raw_input(help_text))

def guess_word(letter_list,letter_dic):
    iteration = 0
    guess_letter_list = []
    while iteration < 6:
        letter = get_input('\nEnter yout letter: ')
        guess_letter_list.append(letter)
        if letter in letter_list:
            for guess in guess_letter_list:
                for j, char in enumerate(letter_list):
                    if char == guess:
                        letter_dic[j] = guess
            print '\n'
            print ' '.join(letter_dic.values())
            if letter_list == letter_dic.values():
                return 1
                break
        else:
            print '\nIncorrect answer'
            if letter in guess_letter_list[:-1]:
                iteration+=0
            else:
                iteration+=1
            print 'You left with %s chances' %(6-iteration)
    return 0

def main():
    print '\nWelcome to Hangman!!! \n'
    words = create_words_list()
    status = 'Y'
    while status == 'Y':
        (letter_list,letter_dic) = random_choice(words)
        print ' '.join(letter_list)
        print '\nGuess a word with letters %s\n%s' %(len(letter_list),' '.join(letter_dic.values()))
        (result) = guess_word(letter_list,letter_dic)
        if result==1:
            print '\nGame completed !!!'
            status = get_input('\nEnter Y to continue and N to stop playing: ')
        else:
            print '\nGame completed, you made 6 incorrect answers'
            status = get_input('\nEnter Y to continue and N to stop playing: ')

if __name__ == '__main__':
    main()