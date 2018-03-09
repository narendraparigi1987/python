import sys
import random

def main():
    i = 0
    a = random.randint(1,3)
    b = 0
    while b != a and b != 'exit':
        i+=1
        c = str(raw_input('enter your guess number: '))
        if c == 'exit':
            break
        else:
            b = int(c)
            if a == b:
                print 'Guess is Matching with random number'
                print 'it took %s guesses to get it right' %(i)
            elif a < b:
                print 'Guess is greater than random number'
            elif a > b:
                print 'Guess is lower than random number'

if __name__ == '__main__':
    main()