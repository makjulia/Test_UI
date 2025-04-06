import allure

from helpers.api.api_data_generate import generate_all_data, generate_all_data_from_response, update_all_data, \
    data_for_update


@allure.epic("Tests")
@allure.feature("API Test Cases")
class TestApi:
    @allure.story("Выполнение запроса на получение списка сущностей")
    @allure.step("Шаги")
    def test_get_all(self,service):
        with allure.step("Шаг - Вызов метода GET"):
            response = service.method_get_all()
        assert response.status_code == 200

    @allure.story("Выполнение запроса на получение одной сущности")
    @allure.step("Шаги")
    def test_get(self,service,obj_id):
        with allure.step("Шаг - Вызов метода GET"):
            response = service.method_get(obj_id).json()
        assert response["id"] == obj_id

    @allure.story("Выполнение запроса на добавление новой сущности")
    @allure.step("Шаги")
    def test_post(self, service):
        with allure.step("Шаг - Составление тела запроса"):
            data = generate_all_data()
        with allure.step("Шаг - Вызов метода POST"):
            response_id = service.method_post(data.model_dump())
        response_get = service.method_get(response_id).json()
        response = generate_all_data_from_response(response_get)
        assert data == response

    @allure.story("Выполнение запроса на обновление сущности и ее дополнений")
    @allure.step("Шаги")
    def test_patch(self,service,obj_id):
        with allure.step("Шаг - Составление тела запроса с новыми дополнениями"):
            obj = service.method_get(obj_id).json()
            data = generate_all_data_from_response(obj)
            new_data = update_all_data(data, data_for_update())
        with allure.step("Шаг - Вызов метода PATCH"):
            response = service.method_patch(obj_id, new_data.model_dump())
        response_get = generate_all_data_from_response(service.method_get(obj_id).json())
        assert new_data == response_get
        assert response.status_code == 204

    @allure.story("Выполнение запроса на удаление сущности и ее дополнений")
    @allure.step("Шаги")
    def test_delete(self,service, obj_id):
        with allure.step("Шаг - Вызов метода DELETE"):
            response = service.method_delete(obj_id)
        assert response.status_code == 204
        response = service.method_get(obj_id)
        assert response.status_code == 500


