import sys
import random

def remove_dup_set(list_name):
    return list(set(list_name))

def remove_dup_loop(list_name):
    remove_dup_list = []
    for i in list_name:
        if i not in remove_dup_list:
            remove_dup_list.append(i)
    return remove_dup_list

def main():
    print 'welcome to List Remove Duplicates session'
    a = [1,1,2,2,3,3,4,4,5,6,7]
    #a = random.sample(range(100),30)
    b = remove_dup_set(a)
    c = remove_dup_loop(a)
    print b
    print c

if __name__ == '__main__':
    main()