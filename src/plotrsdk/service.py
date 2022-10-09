import requests as r
from .utils import get_token


class LOTR:
    def __init__(self):
        self.base_url = "https://the-one-api.dev/v2"

    def prepare_request_url(self, resource, params):
        req = r.PreparedRequest()
        req.prepare_url(self.base_url + "/" + resource, params)
        return req.url

    def make_request(self, method, resource, params={}, headers={}, attach_token=False):
        url = self.prepare_request_url(resource, params)
        if attach_token:
            headers["Authorization"] = f"Bearer {get_token()}"
        # TODO: Add request retry
        return r.request(method, url, headers=headers).json()
