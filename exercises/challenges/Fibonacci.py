import sys
import random

def enter_input(help_text='enter your number: '):
    return int(input(help_text))

def Fibonacci_series(num):
    Fibonacci_List = [1]
    while num >= 0:
        
        if len(Fibonacci_List) > 1:
            prev_prev_num = Fibonacci_List[-2]
        else:
            prev_prev_num = 0
        cur_num = prev_prev_num + Fibonacci_List[-1]
        Fibonacci_List.append(cur_num)
        num -= 1
    return Fibonacci_List

def main():
    num = enter_input('enter your number to generate Fibonacci series: ')
    print 'welcome to generate Fibonacci series ' +str(num)
    Fibonacci_List = Fibonacci_series(num)
    print Fibonacci_List

if __name__ == '__main__':
    main()