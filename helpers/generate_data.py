from faker import Faker
import random


# Функция для генерации данных для поля Post Code
def generate_string_for_post_code():
    return ''.join([str(random.randint(0, 9)) for _ in range(10)])


# Функция для генерации данных для поля First Name
def generate_string_for_first_name(postcode):
    numwords = {num: letter for num, letter in
                enumerate("abcdefghijklmnopqrstuvwxyz")}
    data = [int(i) for i in map(''.join, zip(*([iter(postcode)] * 2)))]
    firstname = ''.join([numwords[i % 26] for i in data])
    return firstname


# Функция для генерации данных для поля Last Name
def generate_last_name():
    fake = Faker("ru_RU")
    last_name = fake.last_name()
    return last_name

# Функция для нахождения средней длины строки в First Name
def get_name_to_delete(names:list[str]) -> str:
    avg_len = sum(map(len, names)) / len(names)
    name = min(names, key=lambda name: abs(avg_len - len(name)))
    return name
