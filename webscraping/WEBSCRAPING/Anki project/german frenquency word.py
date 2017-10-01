import requests
from bs4 import BeautifulSoup
from lxml import etree


headers = {  "chrome_user_agent" : """\
        Mozilla/5.0 (Windows NT 6.3; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/37.0.2049.0 Safari/537.36"""}


def make_soup(url):
    r = requests.get(url,headers=headers)
    # print r.content
    r.raise_for_status()
    soupdata = BeautifulSoup(r.content, 'lxml')
    return soupdata


#url = 'http://www.languagedaily.com/learn-german/vocabulary/common-german-words-3'
url = 'https://translate.google.co.in/#auto/en/tun%0AMann%0Aeuch%0Awer%0Awirklich%0Aihm%0Aeinem%0Awerde%0Asagen%0Adeine%0Adenn%0Adanke%0Aandere%0A%C3%BCber%0Akomm%0Aeiner%0Aeinfach%0Asoll%0Am%C3%BCssen%0Anie%0Agibt%0Ahey%0Ades%0Atut%0ALeben%0Awillst%0Aviel%0Alos%0AZeit%0AIhnen%0Aam%0Aw%C3%BCrde%0Ahatte%0Akannst%0Awissen%0Azur%C3%BCck%0Aheute%0Adamit%0Agesagt%0AIhr%0Amacht%0Awei%C3%9Ft%0Akein%0Awollen%0Awurde%0Awollte%0AFrau%0Aw%C3%A4re%0AGott%0ALeute'
soup = make_soup(url)

print '*'*40
roman_results = [td.find("span") for td in
                     soup.findAll("pre", {"id": "tw-target-rmn"})]
# print roman_results



