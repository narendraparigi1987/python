import sys

def bubble_sort(L):
    swap = False
    while not swap:
        swap = True
        for j in range(1,len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp


def main():
    print 'welcome to bubble sort'
    L = [1,2,4,3]
    print L
    bubble_sort(L)
    print L

if __name__ == '__main__':
    main()