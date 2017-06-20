import urllib
import re

url= ['https://goal.com/en','https://nytimes.com','https://cnn.com']

regex = '<title>(.+?)</title>'
pattern = re.compile(regex)
for dat in range(0,len(url)):
    html = urllib.urlopen(url[dat]).read()
    # print html
    titles = re.findall(pattern,html)
    print titles

    print '*'*30