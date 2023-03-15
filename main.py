import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

movies = soup.find_all("h3")
films = []

for film in movies:
    films.append(film.get_text())

films.reverse()

for film in films:
    print(film)

