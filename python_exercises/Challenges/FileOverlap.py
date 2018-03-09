import sys
import random
import requests
from bs4 import BeautifulSoup

def overlap_compare(List1, List2):
    New_List = []
    for num in List1:
        if num in List2 and num != List1[-1]:
            New_List.append(num)
    return New_List

def main():
    print 'welcome to program'
    open_file_1 = open(r'C:\OneDriveAccenture\One.txt','r')
    open_file_2 = open(r'C:\OneDriveAccenture\Two.txt','r')
    List1 = open_file_1.read().split('\n')
    List2 = open_file_2.read().split('\n')
    result = overlap_compare(sorted([int(x) for x in List1]),sorted([int(y) for y in List2]))
    print result

if __name__ == '__main__':
    main()