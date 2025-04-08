import random

from faker import Faker


def generate_string_for_post_code():
    """Функция для генерации данных для поля Post Code"""
    return " ".join([str(random.randint(0, 9)) for _ in range(10)])



def generate_string_for_first_name(postcode):
    """Функция для генерации данных для поля First Name"""
    numwords = {num: letter for num, letter in
                enumerate("abcdefghijklmnopqrstuvwxyz")}
    data = [int(i) for i in map(''.join, zip(*([iter(postcode)] * 2)))]
    firstname = ''.join([numwords[i % 26] for i in data])
    return firstname



def generate_last_name():
    """Функция для генерации данных для поля Last Name"""
    fake = Faker("ru_RU")
    last_name = fake.last_name()
    return last_name


def get_name_to_delete(names:list[str]) -> str:
    """Функция для нахождения средней длины строки в First Name"""
    avg_len = sum(map(len, names)) / len(names)
    name = min(names, key=lambda name: abs(avg_len - len(name)))
    return name
