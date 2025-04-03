class API_URL:
    BASE_URL = "http://localhost:8080/api"

class Routes(str):
    POST_OBJ = "/create"
    GET_OBJ = "/get/{}"
    DELETE_OBJ = "/delete/{}"
    GET_ALL_OBJ = "/getAll"
    PATCH_OBJ = "/patch/{}"
