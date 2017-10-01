from bs4 import BeautifulSoup
import urllib2, pandas


def makesouap(url):
    html =  urllib2.urlopen(url).read()
    soupdata = BeautifulSoup(html,'lxml')
    return soupdata
soup = makesouap('http://www.goal.com/en/news/12/spanish-football/2016/12/15/30535202/neymar-credits-messi-with-rescuing-barcelona-career?ICID=SP_HN_HP_RI_1_3')
# for data in  soup.find_all('p'):
#     print data.text
# tables = soup.find('table')
# # print tables
# table_row = tables.find_all('tr')
# # print table_row
# table_data = [x.text for x in table_row  ]
# print table_data
# # print tables.text



# for data in soup.find_all('table'):
#     print data.text.strip()
panda  = pandas.read_html('http://www.goal.com/en/news/12/spanish-football/2016/12/15/30535202/neymar-credits-messi-with-rescuing-barcelona-career?ICID=SP_HN_HP_RI_1_3',header=0)
for tab in panda:
    print tab
