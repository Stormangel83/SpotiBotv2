import spotipy
import spotipy.util as util

import os
os.system("cls")

username=os.getenv("SPOTIFY_USERNAME")

scope = 'user-top-read playlist-read-private playlist-modify-private'

token = util.prompt_for_user_token(username,scope,
client_id=os.getenv("SPOTIPY_CLIENT_ID"),
client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"))

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_top_artists(limit=200,offset=0,time_range='long_term')
    for song in range(2):
        list = []
        list.append(results)
else:
    print("Can't get token for", username)

longueur = (len(list[0]['items']))
for i in range(longueur):
    print("Numéro ",i+1," : ",list[0]['items'][i]['name'])
