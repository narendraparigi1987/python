import sys
import random

def get_number(help_text='Enter number: '):
    return int(input(help_text))

def check_matching(source_list,target_list):
    cows  = 0
    bulls = 0
    for i, snum in enumerate(source_list):
        for j, tnum in enumerate(target_list):
            if i == j and snum == tnum:
                cows += 1
            elif i != j and snum == tnum:
                bulls += 1
    return cows, bulls

def main():
    print '\nWelcome to Cows and Bulls Game !!!'
    source=random.randint(1000,9999)
    print source
    target =''
    count = 0
    while source != target and target != 'exit':
        target=get_number('\nEnter number to guess: ')
        cows, bulls = check_matching([int(d) for d in str(source)],[int(d) for d in str(target)])
        count += 1
        if source == target:
            print '%s cows' %(cows), '%s bulls' %(bulls)
            print 'Number of guesses %s' %(count)
            break
        else:
            print '%s cows' %(cows), '%s bulls' %(bulls)

if __name__ == '__main__':
    main()