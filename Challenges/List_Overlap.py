import sys

def main():
    x = range(2,5)
    y = range(7,20)
    z = []
    for i in x:
        if i in y and i not in z:
            z.append(i)
    print 'Numbers %s common to both lists: ' %(z)

if __name__ == '__main__':
    main()