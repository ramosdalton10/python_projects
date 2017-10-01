import requests
from bs4 import BeautifulSoup


def make_soup(url):
    r = requests.get(url)
    r.raise_for_status()
    return BeautifulSoup(r.content, 'lxml')


for x in range(0, 30, 10):
    soup = make_soup('https://www.google.com/search?q=goku#q=goku&start=' + str(x))
    goo ='https://www.google.com/search?q=goku#q=goku&start=' +str(x)
    print goo
    for laptop in soup.find_all(class_='r'):
        print laptop.text.strip('\n')
