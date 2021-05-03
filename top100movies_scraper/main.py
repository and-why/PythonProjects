import requests
from bs4 import BeautifulSoup
import random

top100websites = requests.get("https://www.timeout.com/newyork/movies/best-movies-of-all-time")
soup = BeautifulSoup(top100websites.text, "html.parser")

films = soup.select("h3.card-title a")
film_titles = [title.getText().strip().split(".\xa0")[1] for title in films if len(title.getText().strip().split(".\xa0")) > 1]
# print(film_titles)

with open("movies_list.txt", "w") as file:
    counter = 1
    for film in film_titles:
        file.write(f"{counter}) {film}\n")
        counter += 1

with open("movies_list.txt", "r") as file:
    selection = file.readlines()
    selection = random.choice(selection)
    print(selection)
