import sys

def main():
    string = str(raw_input('enter string for check: '))
    string_len = len(string)-1
    new_string = ''
    while string_len >= 0:
        new_string = new_string+string[string_len]
        string_len=string_len-1
    
    if new_string == string:
        print 'string %s is a palindrome: ' %(string)
    else:
        print 'string %s is not a plaindrome: ' %(string)

if __name__ == '__main__':
    main()