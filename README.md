# Rawkit Playlist
automatically creates a playlist on spotify given a dictionary of artist names/songs. Don't forget to set environment variables.

## Requirements

- Application set up in the [Spotify for Developers](https://developer.spotify.com/)
- The Client ID and Client Secret from the application configured in the Spotify developer portal.

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file to store the required environment variables. the contents of the file should be:

```
SPOTIPY_CLIENT_ID=....
SPOTIPY_CLIENT_SECRET=...
SPOTIPY_REDIRECT_URI=...
```


## Running
```bash
python main.py
```