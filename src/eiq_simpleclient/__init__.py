from furl import furl
import json
from pprint import pprint as pp
import requests
from typing import Any, Dict, List


class APIClient:
    def __init__(self, baseurl: str, apikey: str):
        """Simple Python REST API client for EclecticIQ Intelligence Center (IC).

        :param baseurl: URL to access the REST API endpoint on your IC instance.
            For example: "https://ic-playground.eclecticiq.com/api/beta"
        :type baseurl: str
        :param apikey: API key
        :type apikey: str
        """
        self.baseurl = baseurl
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {apikey}",
            "Accept": "application/json",
        }

    def get(self, path: str, params: Dict[str, str] = {}) -> Dict[str, Any]:
        """Send a GET request to a given endpoint"""
        if path.startswith(self.baseurl):
            f = furl(path)
        else:
            if not path.startswith("/"):
                path = "/" + path
            f = furl(self.baseurl)
            f.path.add(path)
            f.args = params

        r = requests.get(f, headers=self.headers)
        return json.loads(r.text)

    def post(self, path: str, payload: str) -> Dict[str, Any]:
        """Send a POST request to a given endpoint"""
        if not path.startswith("/"):
            path = "/" + path

        f = furl(self.baseurl)
        f.path.add(path)

        r = requests.post(f, headers=self.headers, data=json.dumps(payload))
        return json.loads(r.text)

    def resolve(self, path: str) -> Dict[str, Any]:
        """Retrieves a resources at a given endpoint"""

        # Get only stem of path; omit query parameters
        f = furl(path)
        f.host = furl(self.baseurl).host
        f.scheme = furl(self.baseurl).scheme
        f.args = {}

        return self.get(f.url)
