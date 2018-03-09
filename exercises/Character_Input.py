import sys

def main():
    name = raw_input('enter name :')
    age = int(raw_input('enter age :'))
    target = (2017 - age) + 100
    print 'you will be 100 years on ' + str(target)

if __name__ == '__main__':
    main()