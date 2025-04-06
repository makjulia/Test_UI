from random import randint, choice, choices

from faker import Faker

from api.requests.model import AdditionModel, MainModel


def generate_additional_info():
    """Функция для генерации данных additional_info"""
    fake = Faker("ru_RU")
    return fake.city()

def generate_additional_numb():
    """Функция для генерации данных additional_number"""
    fake = Faker("ru_RU")
    return int(fake.postcode())

def generate_imp_num():
    """Функция для генерации данных important_numbers"""
    return [randint(0, 100) for _ in range(3)]

def generate_title():
    """Функция для генерации данных title"""
    fake = Faker("ru_RU")
    return fake.country()

def generate_verified():
    """Функция для генерации данных verified"""
    return choice([True, False])

def generate_addit_data():
    """Функция для генерации addition"""
    data = {
            "additional_info": generate_additional_info(),
            "additional_number": generate_additional_numb()
    }
    add_model = AdditionModel(**data)
    return add_model

def generate_all_data():
    """Функция для генерации всей тестовой сущности"""
    all_data = {
        "addition": generate_addit_data(),
        "important_numbers": generate_imp_num(),
        "title": generate_title(),
        "verified": generate_verified()
    }
    all_model = MainModel(**all_data)
    return all_model

def generate_all_data_from_response(response: dict):
    """Функция для десериализации полученных данных в объект"""
    all_data = {
        "addition": AdditionModel(**response["addition"]),
        "important_numbers": response["important_numbers"],
        "title": response["title"],
        "verified": response["verified"]
    }
    all_model = MainModel(**all_data)
    return all_model

def update_all_data(all_data: MainModel, new_elem: dict):
    """Функция для обновления данных сущности"""
    new_addit = all_data.addition.model_copy(update=new_elem)
    new_elem["addition"] = new_addit
    new_all_data = all_data.model_copy(update=new_elem)
    return new_all_data

def data_for_update():
    """Функция для генерации данных на обновление сущности"""
    fields = [
        "additional_info",
        "additional_number",
        "addition",
        "important_numbers",
        "title",
        "verified"
    ]
    updated_fields = choices(fields, k=randint(1, len(fields)))
    update_functions = {
        "additional_info": generate_additional_info,
        "additional_number": generate_additional_numb,
        "addition": generate_addit_data,
        "important_numbers": generate_imp_num,
        "title": generate_title,
        "verified": generate_verified
    }
    data_update = {field: update_functions[field]() for field in updated_fields}
    return data_update

