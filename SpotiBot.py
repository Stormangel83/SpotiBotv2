import pytify
import spotipy
import spotipy.util as util
import sys
from icecream import ic

import os
os.system("cls")

username=os.getenv("SPOTIFY_USERNAME")
playlist_id=os.getenv("PLAYLIST_PRINCIPALE")

scope = 'user-top-read playlist-read-private playlist-modify-private'
token = util.prompt_for_user_token(username,scope,client_id=os.getenv("Client_id"),client_secret=os.getenv("Client_secret"),redirect_uri='http://localhost/')

if token:
    spotify = spotipy.Spotify(auth=token)
    spotify.trace = False
else:
    print("Can't get token for", username)

tracklist=pytify.ft_get_tracklist(spotify,username,playlist_id)
decades = pytify.ft_get_decade(tracklist)
allplaylist = pytify.ft_all_playlist_infos(spotify,username)

for decade in decades:
    if (str(decade) not in allplaylist.keys()):
        pytify.ft_create_playlist(spotify,username,decade)

allplaylist = pytify.ft_all_playlist_infos(spotify,username)

for track in tracklist:
    try:
        if track["track"] != None:
      
            print(track["track"]["name"])
        
        i=False

        date_track=pytify.ft_get_song_date(track)
        print(str(date_track))
        tracklist_temp = pytify.ft_get_tracklist(spotify,username,allplaylist[str(date_track)])

        for temp_track in tracklist_temp:  
            if track["track"]["name"] == temp_track["track"]["name"]:
                i=True
                break
                
        if i==False:
                
            spotify.user_playlist_add_tracks(username, allplaylist[str(date_track)], [track["track"]["uri"]])
            
        print("----------------------------")
    except:
        print(track)
