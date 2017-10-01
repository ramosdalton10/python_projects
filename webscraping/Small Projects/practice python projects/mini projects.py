#### EMIAL AND TELEPHONE SCANNER

# import re, pyperclip
# text = pyperclip.paste()
# # print text
# email_regex = re.compile(r'[a-zA-Z0-9._-]+@[a-z]+?.com').findall(text)
# email_book = set()
# for mail in email_regex:
#     email_book.add(mail)
#     # print '\n'.join(email_book)
# print '\n'.join(email_book)
# ##  CHECK IF NUMBER IS PRIME
# import random
# check_number = random.randint(0, 20)
# print check_number
# a = [x for x in range(2,check_number) if check_number % x ==0 ]
# print a
# if len (a) == 0:
#     print 'Prime'
# else:
#     print 'Not Prime'


#######################################################

# The Fibonnaci seqence

#
# import random
# F_number = random.randint(30, 46)
# cont = [1,1]
# for num in range(1,F_number):
#     cont.append(cont[num]+ cont[num-1])
# print cont

###########################################
## PRINT A LIST OF UNIQUE NUMBER FROM THE FIRST LIST
# import random
# import itertools
#
# ran_list = [x for x in range(0,30) if x % 3 ==0]
# ran_list.extend([x for x in range(0,20) if x %1 ==0])
# print list(set(ran_list))

############################################################

## REVERSE WORD ORDER


# text = ' My name is Goku'
#
# a_list = text.split()
# a_list.reverse()
# print ' '.join(a_list)
# # for x in  range(0,len(a_list)):
# #     print a_list[len(a_list)-x-1]

###############################################################

# import string, random, os
#
#
# def ran_pass(y):
#     ran_letter = [random.choice(string.letters) for x in range(0, y)]
#     # print ran_letter
#     ran_num = [str(random.randint(0, 9)) for x in range(0, 9)]
#     ran_letter.extend(ran_num)
#     # print ran_num
#     # print ran_letter
#     totol_gen = [random.choice(ran_letter) for x in range(0, 9)]
#     print totol_gen
#     print ''.join(totol_gen)
#
#
# ran_pass(8)

#########################################################################

### READ PDF

#
#
# import PyPDF2
#
#
# with open('automate-the-boring-stuff-with-python-2015-.pdf','r') as f:
#     pdfreader = PyPDF2.pdfFileReader(f)

##############################################################
# from selenium import webdriver
# import time
# from selenium.webdriver.common import action_chains
#
# browser = webdriver.Firefox()
# # try:
# browser.get('http://gmail.com')
# action = action_chains.ActionChains(browser)
# email_name = browser.find_element_by_id('Email')
# print 'working'
# email_name.send_keys('jokosoko')
# browser.find_element_by_id('next').click()
# print Next_Button
# Next_Button.click()

# browser.implicitly_wait(4)
# password_tag = browser.find_element_by_xpath('//input[@id="Passwd"]')
# print password_tag
# # password_tag.click()
# # if password_tag.is_displayed():
# #     print 'wo'
# password_tag = browser.find_element_by_id('Passwd')
# print password_tag
# browser.implicitly_wait(2)
# password_tag.send_keys('gar123field')
# password_tag.click()
# except:
#     print 'cannot find tag'

# https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1#password
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# browser = webdriver.Firefox()
# browser.get('http://gmail.com')
# action = webdriver.ActionChains(browser)
# emailElem = browser.find_element_by_id('Email')
# print emailElem
# emailElem.send_keys("jokosoko@gmail.com")
# browser.find_element_by_name('signIn').click()
#
# browser.implicitly_wait(2)
# passwordElem = browser.find_element_by_id('Passwd')
# print passwordElem
# try:
#     element = WebDriverWait(passwordElem, 4).until( EC.presence_of_element_located((By.ID, "myDynamicElement")))
# except:
#     passwordElem.send_keys('gar1234field')
#     browser.find_element_by_name('signIn').click()
#     # browser.implicitly_wait(2)
#     browser.quit()
#
#
# # except:
#     # print 'error'
########################################################
# from PIL import Image
# import os
#
# os.chdir('/root/Pictures/')
# print os.getcwd()
# messi =Image.open('messi.jpg')
# print messi.format
# print messi.size
# messi_croped = messi.crop((222,222,1000,666))
# messi_croped.save('messi_croped.jpg')
# messi_croped_1 = Image.open('messi_croped.jpg')
# messi_croped_1.show()


########################################
### DOWNLOAD GERMAN COGNATES

# from bs4 import BeautifulSoup
# import requests
#
# def make_soup(url):
#     r = requests.get(url)
#     r.raise_for_status()
#     soupdata = BeautifulSoup(r.content, 'lxml')
#     return soupdata
# url ='https://www.scribd.com/document/20456363/1300-German-English-Cognates'
# soup = make_soup(url)
# for data in soup.find_all(class_='a'):
#     print data.text

#########################################################


# imput_list = [5,23,11,10,25,30,45,43,56,55,65,60,75,85]
# def cal(num):
#     if num % 5 ==0:
#         return True
#     else:
#         return False
# num_5 = (i for i in imput_list if cal(i))
# [print(i) for i in num_5]
# # for i in num_5:
# #     print i
# ##############################
###GENERATOR FUNCTION EXAMPLE
# correct_code = (9,4,7)
#
# def gen_fun():
#     for x1 in range(10):
#         for x2 in range(10):
#             for x3 in range (10):
#                 yield x1,x2,x3
# for c1,c2,c3, in gen_fun():
#     print c1,c2,c3
#     if (c1,c2,c3) == correct_code:
#         print 'found the combo {0} {1} {2}'.format(c1,c2,c3)
#         break

################################################
#MULTIPROCESSING
###########        MULTIPROCESSING            ####################
# import multiprocessing
#
# def name():
#     print 'Dios'
#
# if __name__ == '__main__':
#     for i in range (100):
#         p = multiprocessing.Process(target=name)
#         p.start()
#         # p.join()


import requests
from  bs4 import BeautifulSoup


url = 'http://www.goal.com'

def makesoup(url):
    html = requests.get(url)
    soupdata = BeautifulSoup(html.content,'lxml')
    return soupdata

soup  = makesoup(url)

