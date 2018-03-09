import sys
import random
import string

def random_select_mixed():
    return random.choice(string.letters+string.digits)

def random_select_uppercase():
    return random.choice(string.ascii_uppercase)

def random_select_lowercase():
    return random.choice(string.ascii_lowercase)

def random_select_digits():
    return random.choice(string.digits)

def random_select_punctuation():
    return random.choice(string.punctuation)

def main():
    print '''chose one of the below
            weak
            strong
          '''
    pwd_type = str(raw_input('enter password type: '))
    pwd = []
    num = 1
    if pwd_type == 'weak':
        while num >= 0:
            pwd.append(random_select_uppercase())
            pwd.append(random_select_lowercase())
            pwd.append(random_select_uppercase())
            pwd.append(random_select_lowercase())
            num -= 1
    elif pwd_type == 'strong':
        while num >= 0:
            pwd.append(random_select_uppercase())
            pwd.append(random_select_lowercase())
            pwd.append(random_select_punctuation())
            pwd.append(random_select_digits())
            pwd.append(random_select_mixed())
            num -= 1
    else:
        print 'Elect correct pwd type'
        exit()
    
    print ''.join(pwd)

if __name__ == '__main__':
    main()