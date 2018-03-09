import sys

def selection_sort(L):
    suffix = 0
    while suffix != len(L):
        for i in range(suffix,len(L)):
            if L[i] < L[suffix]:
                L[suffix],L[i] = L[i], L[suffix]
        suffix+=1

def main():
    print 'welcome to selction sort'
    L = [1,4,3,2]
    print L
    selection_sort(L)
    print L

if __name__ == '__main__':
    main()