import urllib2 , pandas,sys
from urllib2 import HTTPError
from bs4 import BeautifulSoup
from tabulate import tabulate
from stop_words import get_stop_words

def makesouap(url):
    html =  urllib2.urlopen(url).read()
    soupdata = BeautifulSoup(html,'lxml')
    return soupdata

soup = makesouap('https://www.conversationexchange.com/members/messages.php?lg=en&folder=inbox')
print soup.prettify()
try:
    for names in soup.find_all(class_='replied',):
        print names
except HTTPError as he:
    print 'HE'
    exit()
except AttributeError as Ae:
    print 'AE'
    exit()



# pandas.read_html('https://www.conversationexchange.com/members/messages.php?lg=en&folder=inbox')
# print pandas
