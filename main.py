import spotipy
from spotipy.oauth2 import SpotifyOAuth


# authenticating
scope = "playlist-modify-public user-library-read"
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
# user ID for all user parameters in future functions
user_id = spotify.current_user()["id"]

# helper functions

# ASSUMING TRACKS IN A DICT OF [{"artist_name": , "song_name":}]
def compile_track_ids(tracks):
    playlist_ids = []
    for track_info in tracks:
        results = spotify.search(q=f"{ track_info['artist_name'] },{ track_info['song_name'] }")["tracks"]["items"][0]["uri"]
       
        playlist_ids += [results]
    return playlist_ids
    
# searching for songs
# assuming name and track are songs that exist. For some reason Spotipy returns a random song (?) even if the name is misspelled
track_ids = compile_track_ids([{"artist_name":"Radiohead","song_name":"No surprises"}])


def create_playlist(user): 
    user_playlists = spotify.user_playlists(user=user, limit=50, offset=0)["items"]
    for playlist in user_playlists:
        if playlist["name"] == "rawkit":
            spotify.user_playlist_remove_all_occurrences_of_tracks(user=user,playlist_id=playlist["id"],tracks=track_ids)
            return playlist["id"]

 
    spotify.user_playlist_create(user=user,name="rawkit", description="automatically updating playlist with the top 10 songs from rawkit.com")
    create_playlist(user)


# checking if playlist exists - creating if it doesn't already
playlist_id = create_playlist(user_id)

# adding the tracks ids of the songs to the rawkit playlist
spotify.user_playlist_add_tracks(user=user_id,playlist_id=playlist_id,tracks=track_ids)

