
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

# authenticating
scope = "playlist-modify-public user-library-read"
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
# user ID for all user parameters in future functions
user_id = spotify.current_user()["id"]

# helper functions


def compile_track_ids(tracks):
    # ASSUMING TRACKS IN A DICT OF [{"artist_name": , "song_name":}]
    # searching for songs
    # assuming name and track are songs that exist. For some reason Spotipy returns a random song (?) even if the name is misspelled

    playlist_ids = []
    for track_info in tracks:
        results = spotify.search(q=f"{ track_info['artist_name'] },{ track_info['song_name'] }")["tracks"]["items"][0]["uri"]
        playlist_ids += [results]
    return playlist_ids

def clear_playlist(user,playlist_id):
    spotify.user_playlist_remove_all_occurrences_of_tracks(user=user,playlist_id=playlist_id,tracks=[item["track"]["uri"] for item in spotify.user_playlist_tracks(user=user,playlist_id=playlist_id)["items"]])

def create_playlist(user): 
    user_playlists = spotify.user_playlists(user=user, limit=50, offset=0)["items"]
    for playlist in user_playlists:
        if playlist["name"] == "rawkit":            
            return playlist["id"]
 
    spotify.user_playlist_create(user=user,name="rawkit", description="automatically updating playlist with the top 10 songs from rawkit.com")
    create_playlist(user)

def update_playlist(songs):
    # checking if playlist exists - creating if it doesn't already
    playlist_id = create_playlist(user_id)

    # clearing playlist
    clear_playlist(user_id,playlist_id)
    
    # adding the tracks ids of the songs to the rawkit playlist
    spotify.user_playlist_add_tracks(user=user_id,playlist_id=playlist_id,tracks=compile_track_ids(songs))

if __name__ == "__main__":
    update_playlist([{"artist_name":"radiohead","song_name" : "weird fishes"}])