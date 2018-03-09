import sys
import random

def get_input(help_text = 'Give me a number'):
    return int(input(help_text))

def binary_search(n_list,num):
    print 'welcome to binary search algorithm !!! \n'
    
    print n_list
    return_value = 0    
    
    #Looping using while
    while len(n_list) > 2:
    
        if len(n_list) %2 ==0:
            mid_index = len(n_list)/2 -1
        else:
            mid_index = (len(n_list)+1)/2 -1

        if num > n_list[mid_index]:
            n_list = n_list[mid_index:]
        elif num < n_list[mid_index]:
            n_list = n_list[:mid_index]
        elif num == n_list[mid_index]:
            return_value = 1
            break
    
    #returns result
    if return_value != 1:
        if num == n_list[-1] or num == n_list[0]:
            return '\nNumber %s is available in list' %(num)
        else:
            return '\nNumber %s is not available in list' %(num)
    else:
        return '\nNumber %s is available in list' %(num)
    
def main():
    n_list = random.sample(range(1,100),10)
    #n_list = [1, 3, 5, 30, 42, 43, 500]
    num = get_input('Give me a number: ')
    result = binary_search(sorted(n_list),num)
    print result

if __name__ == '__main__':
    main()