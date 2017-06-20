import requests ,re
from bs4 import BeautifulSoup


def make_soup(url):
    r = requests.get(url)
    r.raise_for_status()
    soupdata = BeautifulSoup(r.content, 'lxml')
    return soupdata
patt ='src(.*?)+png'
link = []
for x in range(5):
# soup = make_soup('https://www.google.com/search?q=goku#q=goku&start=40')  # +str(1786 -x))
    soup = make_soup('http://www.xkcd.com/'+str(1784-x))
    comic_data = soup.select('#comic img')
    print  comic_data[0].get('src')
#     for stories in soup.find_all('div',{'id':'comic'}):
#         print stories
#         link_data =str(re.findall(r'src(.*?).png',stories))
#         link.append(link_data)
# print link
# string = '''div id="comic"> img alt="Interest Timescales" src="//imgs.xkcd.com/comics/interest_timescales.png" title="Sometimes, parts of a slowly-rising mountain suddenly rises REALLY fast, which is extra interesting."/>
# </div'''
# match_data = re.findall(r'src(.*?).png',string)
# print match_data

