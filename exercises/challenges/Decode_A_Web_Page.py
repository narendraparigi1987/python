import sys
import random
import requests
from bs4 import BeautifulSoup

def main():
    url = 'http://www.nytimes.com/'
    r = requests.get(url)
    r_html = r.text
    soup = BeautifulSoup(r_html,'html5lib')
    for tag in soup.find_all('h2', {'class': 'story-heading'}):
        try:
            print tag.a.text.strip()
        except:
            pass

if __name__ == '__main__':
    main()