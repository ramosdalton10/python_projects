import mechanize
from bs4 import BeautifulSoup
import urllib2


br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent','Morzilla')]
query = 'https://pythonprogramming.net/navigating-pages-scraping-parsing-beautiful-soup-tutorial/'
br.open(query)
response =  br.follow_link()
urllib2.u






# htmltext = br.open(query).read()
# soup = BeautifulSoup(htmltext,'lxml')
# for data in soup.find_all('div'):
#     print data.a['href']


