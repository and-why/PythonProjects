from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

# date = input("What date are you looking for? Enter in this format: YYYY-MM-DD\n")
top_100_week = "2008-05-04"
website = requests.get(f"https://www.billboard.com/charts/hot-100/{top_100_week}")

soup = BeautifulSoup(website.text, "html.parser")

song_titles = []
song_artists = []

for title in soup.find_all('span', class_="chart-element__information__song"):
    title = title.get_text()
    song_titles.append(title)

for artist in soup.find_all('span', class_="chart-element__information__artist"):
    artist = artist.get_text()
    song_artists.append(artist)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri='http://example.com',
        client_id=os.environ.get('SPOTIPY_CLIENT_ID'),
        client_secret=os.environ.get('SPOTIPY_CLIENT_SECRET'),
        show_dialog=True,
        cache_path="token.txt"
    ))


user_id = sp.current_user()['id']

# create playlist

spotify_user = user_id
playlist = sp.user_playlist_create(user=spotify_user, name=f'Billboard Top100 for {top_100_week}', public=False,
                        description=f'Top 100 for the week of {top_100_week}')

playlist_id = playlist['id']
song_list = []

for i in range(0, len(song_artists) - 1):
    artist = song_artists[i]
    title = song_titles[i]
    results = sp.search(q=f"{title}+{artist}", type='track')
    song_uri = results['tracks']['items']
    if len(song_uri) > 0:
        song_list.append(song_uri[0]['uri'])

sp.playlist_add_items(playlist_id=playlist_id, items=song_list, position=None)

