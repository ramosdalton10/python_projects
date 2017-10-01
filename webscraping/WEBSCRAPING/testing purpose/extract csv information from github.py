import urllib2 , pandas as pd
import requests
from bs4 import BeautifulSoup
import

def maksoup(url):
    html = urllib2.urlopen(url).read()
    soupdata = BeautifulSoup(html,'lxml')
    return soupdata
soup = maksoup('https://github.com/seekshreyas/i257-ZakumiFootball/blob/master/csv_files/players.csv')


# for tb in soup.find_all(class_='js-csv-data csv-data js-file-line-container'):
    # print tb.text
url = 'https://raw.githubusercontent.com/seekshreyas/i257-ZakumiFootball/master/csv_files/players.csv'
# for table in pd.read_html(url):
#     print table


# with open('players.csv','r') as file:
#     print file.read()
csv_data = pd.read_csv('players.csv',header=None)
csv_data.columns = ['S.No','Name','Year','Country','Point', 'Address','Club','League','Link']
five_csv_data =csv_data.head()
# five_csv_data.align(join='inner')
print five_csv_data
five_csv_data.to_excel('players.xlsx')