import sys
import random

def dict_list(list_words):  
    dict_words = {}
    prev_word = ''
    for word in sorted(list_words):
        if prev_word == word:
            dict_words[word] = dict_words[word]+ 1
        else:
            dict_words[word] = 1
        prev_word = word
    return dict_words

def main():
    open_file=open(r'C:\OneDriveAccenture\nameslist.txt','r')
    text = open_file.read()
    text_words = text.split('^')
    dict_words = dict_list(text_words)    
    for a,b in dict_words.items():
        print a +' = '+str(b)

if __name__ == '__main__':
    main()