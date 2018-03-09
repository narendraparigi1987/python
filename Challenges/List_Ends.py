import sys
import random

def first_last_list(list):
    return [i for i in list if i == list[-1] or i == list[0]]

def main():
    #a = [5, 10, 15, 20, 25]
    a = random.sample(range(100), 20)
    b = first_last_list(a)
    print b

if __name__ == '__main__':
    main()