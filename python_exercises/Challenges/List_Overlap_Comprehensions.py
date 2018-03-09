import sys
import random

def main():
    #a = random.sample(range(100),10)
    #b = random.sample(range(100),20)
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    c = [num for i,num in enumerate(a) if num in b and num not in a[i+1:]]
    print c

if __name__ == '__main__':
    main()