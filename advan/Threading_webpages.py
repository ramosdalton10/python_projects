from  threading import Thread
import time
import requests
import re

signs = 'MSFT GOOGL AAPL SSNLF'.split()


def makesoup(url):
    html = requests.get(url)
    regex = '<span id="ref_[^.]*_l">(.+?)</span>'
    pattern = re.compile(regex)
    values = re.findall(pattern, html.content)
    print values[0]
    # soupdata = BeautifulSoup(html.content, 'lxml')
    # return soupdata


def timer():
    time.sleep(4)
    print 'threading'

def main():
    threadlist = []
    for symbols in signs:   # loops throught the links
        url = 'https://www.google.com/finance?q=' + symbols
        # soup = makesoup(url)

        t1 = Thread(target=makesoup, args=(str(url),)) # take the function as the target and arguments
        t1.start()
        # t2 = Thread(target=timer, args=None)
        # t2.start
        threadlist.append(t1) # make a thread list which later wil be joined
    for tread in threadlist:
        tread.join()
if __name__=='__main__': #
    main()