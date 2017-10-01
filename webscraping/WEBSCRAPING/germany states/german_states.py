from bs4 import BeautifulSoup
import requests, random

url = 'https://quizlet.com/649284/germany-states-and-their-capitals-flash-cards/'


# Create a soup function to extract the data
def make_soup(urlnew):
    # html = urllib2.urlopen(url)

    try:
        html = requests.get(url)
        html.raise_for_status()
    except Exception as exc:
        print 'there was a error'
    return BeautifulSoup(html.content, 'xml')


soup = make_soup(url)
cities = []
capitals = []
# loop through the data to get the states and capitals
for x in soup.find_all(class_='SetPageTerm-wordText'):
    cities.append(x.text.encode())
for y in soup.find_all(class_='SetPageTerm-definition'):
    capitals.append(y.text.encode())
# print len(cities)
dict_cap = {}
# creata a list for state and capitals and add data
for y in range(0, len(cities)):
    # print cities[y] + '  - ' +capitals[y]
    dict_cap[cities[y].encode()] = capitals[y].encode()
random.shuffle(cities)
random.shuffle(capitals)
print dict_cap
# test_data = []
# random_num = []
# ask = [capitals[x].encode() for x in range(0,3) if random.choice(cities[x])  not in test_data]
# to get unique set of three capitals without repeat
# for x in range(0, 3):
#     while True:
#         randomindex = random.randint(0, len(capitals))  # select a randon number
#
#         if randomindex not in random_num and len(random_num) < 3:  # check if number already added to the list
#             random_num.append(randomindex)
#             # print randomindex
#             test_data.append(capitals[randomindex].encode())
#         else:
#             break
#
# print test_data
# print capitals
# print cities
# question = []
# answer_to_question = []
for y in cities:
    question = y
    answer_to_question = dict_cap[y]
    wrong_answers_all = dict_cap.values()
    del wrong_answers_all[wrong_answers_all.index(answer_to_question)]
    print question + ' ' + answer_to_question
    option = random.sample(wrong_answers_all, 3)
    option.append(answer_to_question)
    print random.sample(option, 4)
    # print wer
