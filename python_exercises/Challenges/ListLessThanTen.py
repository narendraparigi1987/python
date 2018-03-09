import sys

def main():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = []
    c = []
    num = int(input('enter number: '))
    for i in a:
        if i < 5:
            b.append(i)
        if i < num:
            c.append(i)
    print 'Numbers less than input number %s: ' %(c)
    print 'Number less than number 5 %s: ' %(b)

if __name__ == '__main__':
    main()