import urllib , requests
from bs4 import BeautifulSoup
## PROGRAM TO DOWNLOAD IMAGES FROM NET
def makesouap(url):
    html = requests.get(url)
    soupdata = BeautifulSoup(html.content, 'lxml')
    return soupdata
soup = makesouap('http://www.wou.edu/~rrogers/Germany/Stuttgart%204-18-07/')
images = []
for link in soup.find_all('a'):
    images.append(link.text)
print images[7]
for x in images[6:]:
    print x
    # urllib.urlretrieve('http://www.wou.edu/~rrogers/Germany/Stuttgart%204-18-07/'+str(x),str(x))