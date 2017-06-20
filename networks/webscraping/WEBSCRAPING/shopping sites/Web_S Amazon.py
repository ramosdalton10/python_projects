from bs4 import BeautifulSoup
import requests

def make_soup(url):
    r = requests.get(url)
    r.raise_for_status()
    soupdata = BeautifulSoup(r.content, 'lxml')
    return soupdata
try:
    soup = make_soup('http://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Delectronics&field-keywords=laptop+&sprefix=laptop%2Caps%2C336&crid=JXVIYSTEBCRX')
    for laptop in soup.find_all(class_='a-row a-spacing-mini'):
        print laptop.text.strip()
except:
        print 'page is not loading'