from bs4 import  BeautifulSoup
import urlparse
import requests

htmltext = requests.get('https://nytimes.com')
soup = BeautifulSoup(htmltext.content,'lxml')
for tag in soup.find_all('a',href=True):
    # print tag
    l1 =urlparse.urlparse(tag['href']).hostname
    l2 =urlparse.urlparse(tag['href']).path
    print 'https://'+str(l1)+l2