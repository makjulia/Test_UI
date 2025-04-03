from random import randint, choice

from faker import Faker

from api.requests.model import AdditionModel, MainModel


def generate_additional_info():
    """Функция для генерации данных additional_info"""
    fake = Faker("ru_RU")
    return fake.city()

def generate_additional_numb():
    """Функция для генерации данных additional_number"""
    fake = Faker("ru_RU")
    return fake.postcode()

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
