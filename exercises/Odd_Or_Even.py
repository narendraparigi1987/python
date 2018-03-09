import sys

def main():
    num = int(input('enter number to check: '))
    check = int(input('enter number to divide with: '))
    
    if num % 2 == 0:
        print 'number %s is even' %(num)
    elif num%2 != 0:
        print 'number %s is odd' %(num)

    if num % 4 == 0:
        print 'number %s is multiple of four' %(num)
    else:
        print 'number %s is not a multiple of four' %(num)
    
    if num % check ==0:
        print 'number %s is divisible by %s' %(num,check)
    else:
        print 'number %s is not divisible by %s' %(num,check)

if __name__ == '__main__':
    main()