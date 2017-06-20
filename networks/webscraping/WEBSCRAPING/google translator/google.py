import requests
from bs4 import BeautifulSoup
import mechanize

# url = 'https://translate.google.co.in/translate_a/single?client=t&sl=auto&tl=es&hl=en&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&source=bh&ssel=0&tsel=0&kc=1&tk=581799.963439&q=catch'

headers = {"chrome_user_agent": """\
        Mozilla/5.0 (Windows NT 6.3; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/37.0.2049.0 Safari/537.36"""}

# def makesoup(url):
#     htmltext = requests.get(url, headers=headers)
#     # print htmltext.content
#     soupdata = BeautifulSoup(htmltext.content,'lxml')
#     return soupdata
#
# soup = makesoup(url)
# print soup.find_all()
# def translator (n_lan,t_lan,text):
#     url = 'https://translate.google.co.in/translate_a/single?client=t&sl='+n_lan+'&tl='+t_lan+'&hl=en&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&source=bh&ssel=0&tsel=0&kc=1&tk=581799.963439&q='+text
#     htmltext_old = requests.get(url, headers=headers)
#     htmltext =  htmltext_old.content#.split(']]')[0].replace('null','').replace(',,,','').replace('[[[','').decode('UTF-8')
#     print htmltext#.split(',')[0].replace('[[[','').replace('"','')
#     print htmltext#.split(',')[1].replace('"','')



# def translator (n_lan,t_lan,text):
url = 'https://translate.google.co.in/translate_a/single?client=t&sl=auto&tl=es&hl=en&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&source=bh&ssel=0&tsel=0&kc=1&tk=581799.963439&q=catched'
# url = 'https://translate.google.co.in/translate_a/single?client=t&sl='+n_lan+'&tl='+t_lan+'&hl=en&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&source=bh&ssel=0&tsel=0&kc=1&tk=581799.963439&q='+text
broswer = mechanize.Browser()
broswer.set_handle_robots(False)
broswer.addheaders = [('User-agent', 'Chrome')]
trans_text = broswer.open(url).read()
# return trans_text
print trans_text.replace(']]]', '').split(',')[0].replace('[[[',
                                                          '')  # replace(']]]','').replace('null','').replace(',,,','')
print trans_text.replace(']]]', '').split(',')[1]  # replace(']]]','').replace('null','').replace(',,,','')

# print translator('en','es','check this side')
