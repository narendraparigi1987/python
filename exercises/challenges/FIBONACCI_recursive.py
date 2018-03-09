import sys

def fibinacci(n):
    if n==0 or n==1:
        return 1
    else:
        return fibinacci(n-1) + fibinacci(n-2)

def main():
    print fibinacci(6)

if __name__ == '__main__':
    main()