import spotipy
import os
import spotipy.util as util

os.system("cls")

playlist_id_primaire=os.getenv("PLAYLIST_PRINCIPALE")
playlist_id_secondaire=os.getenv("PLAYLIST_SECONDAIRE")

username=os.getenv("SPOTIFY_USERNAME")
scope = 'user-top-read playlist-read-private playlist-modify-private'

token = util.prompt_for_user_token(username,scope,
client_id=os.getenv("SPOTIPY_CLIENT_ID"),
client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"))

if token:
    spotify = spotipy.Spotify(auth=token)
    spotify.trace = False
else:
    print("Can't get token for", username)


results = spotify.user_playlist_tracks(username,playlist_id_primaire)
tracks_prim = results['items']
while results['next']:
    results = spotify.next(results)
    tracks_prim.extend(results['items'])



results = spotify.user_playlist_tracks(username,playlist_id_secondaire)
tracks_sec = results['items']
while results['next']:
    results = spotify.next(results)
    tracks_sec.extend(results['items'])


track_list_prim=[]
track_list_sec=[]

for track_sec in tracks_sec:
    try:
        tracksec=track_sec["track"]["name"]
        track_list_sec.append(tracksec)
    except:
        pass

for track_prim in tracks_prim:
    try:
        spotify.user_playlist_add_tracks(username, playlist_id_secondaire, [track_prim["track"]["uri"]])
        if (track_prim["track"]["name"] not in track_list_sec):
            spotify.user_playlist_add_tracks(username, playlist_id_secondaire, [track_prim["track"]["uri"]])
    except:
        pass
