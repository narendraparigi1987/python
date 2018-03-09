import sys

def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
        
def main():
    result = factorial(3)
    print result

if __name__ == '__main__':
    main()