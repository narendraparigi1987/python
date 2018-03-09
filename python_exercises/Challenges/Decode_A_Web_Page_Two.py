import sys
import random
import requests
from bs4 import BeautifulSoup

def main():
    url = 'http://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
    r = requests.get(url)
    r_html = r.text
    soup = BeautifulSoup(r_html,'html5lib')
    
    for paragraph in soup.find_all('div', {"class:", "dek"}):
        try:
            print paragraph.text
        except:
            pass

    #for paragraph in soup.find_all('section', {"class:" , "content-section"}):
    #    try:
    #        print paragraph.text
    #    except:
    #        pass

if __name__ == '__main__':
    main()
