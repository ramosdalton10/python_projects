import re, requests
from bs4 import BeautifulSoup
import urllib

# urls = ['http://edition.cnn.com','http://ndtv.com', 'http://nytimes.com/sport/formula1']
# i = 0
# # while i < len(urls):
# #     html = requests.get(urls[i]).content
# #     patern ='<title>(.*?)</title>'
# #     findTitle = re.findall(patern,html)
# #     print findTitle
# #     print '*'*70
# #     i+=1
# #Another Way would be to use Beautiful Soap
# while i < len(urls):
#     html = requests.get(urls[i]).content
#     soup = BeautifulSoup(html,'lxml')
#     soupdata = soup.find_all('title')
#     print soupdata
#     print '*'*70
#   i+=1

##########################################################
from bs4 import BeautifulSoup
import requests


def makesoup(url):
    htmltext = requests.get(url).content
    soupdata = BeautifulSoup(htmltext, 'lxml')
    return soupdata


soup = makesoup('http://nytimes.com')
# title =  soup.find_all(class_='story-heading')
# for text in  title:
#     # print text.text.strip()
#     if
for data in soup.find_all(class_='story-heading',):
    # print data.a['href']
    print data.text.strip()
# links_data = [x.a['href'] for x in  soup.find_all(class_='story-heading')]
# print links_data

