from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import numpy as np

def main():
    movies = getMovies("http://movie.naver.com/movie/preview/index.nhn")
    print(np.array(scrapPreview(movies)))
    '''
    if title == None:
        print("Title could not be found")
    else:
        print("That is all")
    '''
def getMovies(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        movies = bsObj.find('ul',attrs={'class':'prize_list'}).findAll('li')
    except AttributeError as e:
        return None
    return movies
    
def scrapPreview(movies):
    preview_list = []
    naver_movie_url = "http://movie.naver.com"
    labels = ['title','link']
    preview_list.append(labels)
    
    for movie in movies:
        preview_info = []
        preview_info.append(movie.dl.dt.a['title'])
        preview_info.append(naver_movie_url + movie.dl.dt.a['href'])
       # print(movie.dl.dd.)
        preview_list.append(preview_info)
    
    return preview_list
    
if __name__ == "__main__":
    main()