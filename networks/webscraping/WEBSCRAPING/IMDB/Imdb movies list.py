import requests
# from urllib2 import HTTPError
from bs4 import BeautifulSoup
from pandas import


def makesouap(url):
    html = requests.get(url).content
    soupdata = BeautifulSoup(html,'html.parser')
    return soupdata


soup = makesouap('http://www.imdb.com/chart/top?ref_=nv_mv_250_6')
Movie_Name = []
Rank = []
Year = []
for movies in soup.find_all(class_='titleColumn'): 
    rank, movie, years = movies.text.strip().split('\n')
    Rank.append(rank)
    Movie_Name.append(movie)
    Year.append(years)

dict_movie_data = {'Ranking': Rank, 'Year': Year, 'wMovie Name': Movie_Name}
# pd_data = pd.DataFrame(dict_movie_data)
# print pd_data
print [item.encode('UTF-8') for item in Movie_Name]
# print rank +' ' + name_of_the_movies +' ' + year
# pd_formating = {'rank':rank,'year':years,'Name':movies}
# dat = pandas.read_html('http://www.imdb.com/chart/top?ref_=nv_mv_250_6')

