import requests
from config import s_refresh_token, s_encode


class Refresh:
    def __init__(self):
        self.refresh_token = s_refresh_token
        self.s_encode = s_encode

    def refresh(self):
        query = 'https://accounts.spotify.com/api/token'
        response = requests.post(
            query,
            data={'grant_type': "refresh_token",
                  "refresh_token": s_refresh_token},
            headers={
                'Authorization': 'Basic ' + s_encode
            }
        )
        return response.json()['access_token']


a = Refresh()
a.refresh()
