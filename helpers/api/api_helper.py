from api.requests.base_requests import BaseApi

from config.config import APIUrl, Routes


class ServiceApi(BaseApi):

    def __init__(self):
        self.base_url = APIUrl.BASE_URL

    def method_post(self, data):
        post_url = self.base_url + Routes.POST_OBJ
        return self.request_post(url=post_url, json=data).json()

    def method_get(self, id_entity):
        get_url = self.base_url + Routes.GET_OBJ.format(id_entity)
        return self.request_get(url=get_url)

    def method_delete(self, id_entity):
        delete_url = self.base_url + Routes.DELETE_OBJ.format(id_entity)
        return self.request_delete(url=delete_url)

    def method_get_all(self):
        get_all_url = self.base_url + Routes.GET_ALL_OBJ
        return self.request_get(url=get_all_url)

    def method_patch(self, id_entity, data):
        patch_url = self.base_url + Routes.PATCH_OBJ.format(id_entity)
        return self.request_patch(url=patch_url, json=data)
