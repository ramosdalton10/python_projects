import urllib
import re
import requests

headers = {  "chrome_user_agent" : """\
        Mozilla/5.0 (Windows NT 6.3; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/37.0.2049.0 Safari/537.36"""}
url = 'https://www.google.com/finance?q=google'
html =  requests.get(url,headers=headers)
# html = urllib.urlopen('http://finance.yahoo.com/quote/AAPL/holders?p=AAPL').read()
# print html.content
regex= '<span id="ref_[^.]*_l">(.+?)</span>'

pattern = re.compile(regex)
price = re.findall(pattern,html.content)
print price[0]