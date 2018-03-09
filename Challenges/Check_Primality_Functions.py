import sys
import random

def get_input(help_text='Give me a number: '):
    return (int(input(help_text)))

def check_primality(list,num):
    for i in list:
        if num % i == 0 and i != 1 and i != num:
            b = 0
            break
        else:
            b = 1
    return b

def main():
    num = get_input('Enter number to check for Primality: ')
    a = range(1,num+1)
    b = check_primality(a,num)
    if b == 1:
        print 'Give number %s is a prime' %(str(num))
    else:
        print 'Give number %s is a not prime' %(str(num))

if __name__ == '__main__':
    main()