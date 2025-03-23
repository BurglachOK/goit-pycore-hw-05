import sys
from pathlib import Path


def parse_log_line(line: str) -> dict:
    date, time, level = line.split()[:3]
    message = ' '.join(line.split()[3:])
    parsed_line = {
        'date': date,
        'time': time,
        'level': level,
        'message': message
    }
    return parsed_line


def load_logs(file_path: str) -> list:
    with open(file_path, 'r') as file:
        for line in file:
            yield parse_log_line(line)


def filter_logs_by_level(logs: list, level: str) -> list:
    for log in logs:
        if log['level'] == level:
            yield log


def count_logs_by_level(logs: list) -> dict:
    pass


def display_log_counts(counts: dict):
    pass


def print_logs(logs: list):
    for log in logs:
        print(log)


print(print_logs(load_logs(Path('./log.log'))))

# print(parse_log_line('2021-07-01 12:00:00 INFO This is an info message'))



# Завдання 4

# Доробіть консольного бота помічника з попереднього домашнього завдання та додайте обробку помилок за допомоги декораторів.



# Вимоги до завдання:

# Всі помилки введення користувача повинні оброблятися за допомогою декоратора input_error. Цей декоратор відповідає за повернення користувачеві повідомлень типу "Enter user name", "Give me name and phone please" тощо.
# Декоратор input_error повинен обробляти винятки, що виникають у функціях - handler і це винятки: KeyError, ValueError, IndexError. Коли відбувається виняток декоратор повинен повертати відповідну відповідь користувачеві. Виконання програми при цьому не припиняється.


# Рекомендації для виконання:

# В якості прикладу додамо декоратор input_error для обробки помилки ValueError

# def input_error(func):
#     def inner(*args, **kwargs):
#         try:
#             return func(*args, **kwargs)
#         except ValueError:
#             return "Give me name and phone please."

#     return inner



# Та обгорнемо декоратором функцію add_contact нашого бота, щоб ми почали обробляти помилку ValueError.

# @input_error
# def add_contact(args, contacts):
#     name, phone = args
#     contacts[name] = phone
#     return "Contact added."



# Вам треба додати обробники до інших команд (функцій), та додати в декоратор обробку винятків інших типів з відповідними повідомленнями.



# Критерії оцінювання:

# Наявність декоратора input_error, який обробляє помилки введення користувача для всіх команд.
# Обробка помилок типу KeyError, ValueError, IndexError у функціях за допомогою декоратора input_error.
# Кожна функція для обробки команд має власний декоратор input_error, який обробляє відповідні помилки і повертає відповідні повідомлення про помилку.
# Коректна реакція бота на різні команди та обробка помилок введення без завершення програми.


# Приклад використання:

# При запуску скрипту діалог з ботом повинен бути схожим на цей.

# Enter a command: add
# Enter the argument for the command
# Enter a command: add Bob
# Enter the argument for the command
# Enter a command: add Jime 0501234356
# Contact added.
# Enter a command: phone
# Enter the argument for the command
# Enter a command: all
# Jime: 0501234356 
# Enter a command: