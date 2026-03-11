import requests


class HttpClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def post(self, endpoint: str, json=None, data=None):
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, json=json, data=data)

    def get(self, endpoint: str, params=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url, params=params, headers=headers)
