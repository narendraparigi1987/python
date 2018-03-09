import sys

def main():
     x = range(2,11)
     y = []
     num = int(input('enter number to find divisors: '))
     for i in x:
         if num % i == 0:
           y.append(i)  
     print 'Divisors for number %s are %s ' %(num,y)

if __name__ == '__main__':
    main()