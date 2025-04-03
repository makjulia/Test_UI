from helpers.api.api_data_generate import generate_all_data


class TestApi:

    # def test_post(self, service):
    #     data = generate_all_data().model_dump()
    #     response = service.method_post(data)
    #     print(response)

    # def test_get(self,service):
    #     response = service.method_get(10)
    #     print(response)
    # #
    # def test_get_all(self,service):
    #     response = service.method_get_all()
    #     print(response)

    # def test_delete(self,service):
    #     response = service.method_delete(11)
    #     print(response)

    def test_patch(self,service):
        data = generate_all_data().model_dump()
        response = service.method_patch(2, data)
        print(service.method_get(2))
