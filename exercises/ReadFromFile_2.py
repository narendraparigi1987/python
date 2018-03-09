import sys
import random

diction = {}

def dict_words(line_key):
    if line_key in diction:
        diction[line_key] = diction[line_key]+1
    else:
        diction[line_key] = 1

def main():
    print '\nwelcome to categorization!!!'
    
    open_file = open(r'C:\OneDriveAccenture\category.txt','r')
    open_file_w = open(r'C:\OneDriveAccenture\category_output.txt','w')
    
    lines = open_file.readlines()
    prev_line_check = ''
    
    for line in lines:
        line_list = line.split('/')[::-1]
        line_key = '/'.join(line_list[1:][::-1]).strip()
        line_check = ''.join(line_list[0]).strip()
        
        if prev_line_check == line_check:
            pass
        else:
            dict_words(line_key)
        
        prev_line_check = line_check

    for i,j in diction.items():
            open_file_w.write(i+'='+str(j)+'\n')

if __name__ == '__main__':
    main()