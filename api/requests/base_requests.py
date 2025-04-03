import requests



class BaseApi:

    def request_post(self, **kwargs):
        return requests.post(**kwargs)

    def request_get(self, **kwargs):
        return requests.get(**kwargs)

    def request_delete(self, **kwargs):
        return requests.delete(**kwargs)

    def request_patch(self, **kwargs):
        return requests.patch(**kwargs)