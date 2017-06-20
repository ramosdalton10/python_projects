from bs4 import BeautifulSoup
import requests


headers = {  "chrome_user_agent" : """\
        Mozilla/5.0 (Windows NT 6.3; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/37.0.2049.0 Safari/537.36"""}

def make_soup(url):
    r = requests.get(url,headers=headers)
    r.raise_for_status()
    soupdata = BeautifulSoup(r.content, 'lxml')
    return soupdata
url ='https://www.scribd.com/document/20456363/1300-German-English-Cognates'
soup = make_soup(url)


with open('german.txt','a') as f:
    for data in soup.find_all(class_='a'):
    # f.write(data.text.encode('utf-8'))
        f.writelines(data.text.encode('utf-8'))

        print data.text
f.close()
