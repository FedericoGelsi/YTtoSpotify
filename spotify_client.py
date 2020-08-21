import requests
import urllib.parse

class SpotifyClient(object):
    def __init__(self, api_token):
        self.api_token = "BQC_Xsu3FyrArVYIXTpIWXDhwX8JG_DE6PoPhRrAbIE43wFfmpQG1ilzK4FlxxqAKXgyprhrKWCkrzD-JCnUe2NIi5Wimy8-7K7Rr0Yh_cxW2Zmsil_4KrMm7XRiTnPzRnm7tkddt_NtKk5etDy63Q8OM3A"

    def search_song(self, track):
        track = ' '.join(track.split(' ',2)[:2])
        query = urllib.parse.quote(track)
        print(query)
        url = f"https://api.spotify.com/v1/search?q={query}&type=track&market=AR&limit=1"

        response = requests.get(
            url,
            headers={
                'Accept': 'application / json',
                'Content-Type': "application/json",
                "Authorization": f"Bearer {self.api_token}"
            }
        )

        response_json = response.json()
        results = response_json['tracks']['items']
        if results:
            return results[0]['id']
        else:
            raise Exception(f"No song found for {track}")

    def add_song_to_spotify(self, song_id):
        url = "https://api.spotify.com/v1/me/tracks"
        response = requests.put(
            url,
            json={
                "ids": [song_id]
            },
            headers={
                'Content-Type': "application/json",
                "Authorization": f"Bearer {self.api_token}"
            }
        )
        return response.ok
