import requests
from bs4 import BeautifulSoup

with requests.session() as s:
    url = 'https://www.conversationexchange.com/members/login.php?lg=en&login'
    Username = 'jokosoko@gmail.com'
    Password = 'garfield'
    s.get(url)
    Login_Data = dict (username=Username, password=Password )
    s.post(url,data=Login_Data,headers={'Referer':'https://www.conversationexchange.com/'})
    page = s.get('https://www.conversationexchange.com/index.php?lg=en')
    # print page.content

soup = BeautifulSoup(page.content,'lxml')
print soup.find(class_='drop clickable')