from api.requests.base_requests import BaseApi

from config.config import API_URL, Routes


class ServiceApi(BaseApi):

    def __init__(self):
        self.base_url = API_URL.BASE_URL


    def method_post(self, data):
        post_url = self.base_url + Routes.POST_OBJ
        return self.request_post(url=post_url, json=data).json()


    def method_get(self, id):
        get_url = self.base_url + Routes.GET_OBJ.format(id)
        return self.request_get(url=get_url).json()

    def method_delete(self, id):
        delete_url = self.base_url + Routes.DELETE_OBJ.format(id)
        return self.request_delete(url=delete_url)

    def method_get_all(self):
        get_all_url = self.base_url + Routes.GET_ALL_OBJ
        return self.request_get(url=get_all_url).json()

    def method_patch(self, id, data):
        patch_url = self.base_url + Routes.PATCH_OBJ.format(id)
        return self.request_patch(url=patch_url, json=data)