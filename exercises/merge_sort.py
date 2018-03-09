import sys

def merge(left,right):
    result = []
    i,j = 0,0
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    while i < len(left):
        result.append(left[i])
        i+=1
    while j < len(right):
        result.append(right[j])
        j+=1
    return result

def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        half = len(L)//2
        left = merge_sort(L[:half])
        right = merge_sort(L[half:])
        return merge(left,right)

def main():
    print 'welcome to merge sort'
    L = [1,4,3,2]
    print L
    print merge_sort(L)
    print L

if __name__ == '__main__':
    main()