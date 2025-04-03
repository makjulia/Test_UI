from helpers.api.api_helper import ServiceApi

x = ServiceApi()
data = {"addition": {"additional_info": "Заголовок №2", "additional_number": 565},"important_numbers": [42, 87, 15], "title": "Заголовок сущности", "verified": True}
#x.method_post(data)

id = 3
data_2 = {"addition": {"additional_info": "Заголовок №5", "additional_number": 796},"important_numbers": [42, 87, 15], "title": "Заголовок сущности", "verified": True}
# print(x.method_get(id))
print(x.method_get_all())

# x.method_patch(3, data_2 )
# print(x.method_get(id))
#
# #x.method_delete(id)
# print(x.method_get(id))