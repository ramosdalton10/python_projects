import requests
from bs4 import BeautifulSoup



def make_soup(url):
    r = requests.get(url)
    soupdata = BeautifulSoup(r.content, 'lxml')
    return soupdata

soup = make_soup('http://www.ndtv.com/world-news?pfrom=home-topnavigation2016')
for stories in soup.find_all(class_='nstory_header'):
    print stories.text.replace('\n', '').strip()
    # with open('webscraping_text.txt', 'r+') as f:
        # for x in f:
            # print x.write()
        # print f.write()
            # x.write(stories.text.replace('\n', '').strip())
        # f.write(stories.text.replace('\n', '').strip())
        # f.close()
# with  open('webscraping_text.txt', 'r') as f:
#     f.read()