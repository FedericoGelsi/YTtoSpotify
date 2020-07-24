import os

from youtube_client import YouTubeClient
from spotify_client import SpotifyClient


def run():
    youtube_client = YouTubeClient('./creds/client_secret.json')
    spotify_client = SpotifyClient(os.getenv('SPOTIFY_AUTH_TOKEN'))
    playlists = youtube_client.get_playlist()

    for index, playlist in enumerate(playlists):
        print(f"{index}: {playlist.title}")

    choice = int(input("Enter your choice: "))
    chosen_playlist = playlists[choice]
    print(f"You selected: {chosen_playlist.title}")

    songs = youtube_client.get_videos_from_playlist(chosen_playlist.id)
    print(f"Attempting to add {len(songs)} songs")

    for song in songs:
        spotify_song_id = spotify_client.search_song(song.track)
        if spotify_song_id:
            print(f"Attempting to add {spotify_song_id}")
            added_song = spotify_client.add_song_to_spotify(spotify_song_id)
            if added_song:
                print(f"Added {song.track}")


if __name__ == '__main__':
    run()
