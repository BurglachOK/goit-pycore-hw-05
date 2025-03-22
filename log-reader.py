def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found." 
        except IndexError:
            return "Enter user name."
    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, phone = args
    if   name in contacts:
        contacts[name] = phone
        return "Contact updated."
    return "Contact not found."


@input_error
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    return "Contact not found."


@input_error
def show_all(contacts):
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    return "No contacts found."


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ("close", "exit"):
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
















# Завдання 3 (не обов'язкове)

# Розробіть Python-скрипт для аналізу файлів логів. Скрипт повинен вміти читати лог-файл, переданий як аргумент командного рядка, і виводити статистику за рівнями логування наприклад, INFO, ERROR, DEBUG. Також користувач може вказати рівень логування як другий аргумент командного рядка, щоб отримати всі записи цього рівня.



# Файли логів – це файли, що містять записи про події, які відбулися в операційній системі, програмному забезпеченні або інших системах. Вони допомагають відстежувати та аналізувати поведінку системи, виявляти та діагностувати проблеми.



# Для виконання завдання візьміть наступний приклад лог-файлу:

# 2024-01-22 08:30:01 INFO User logged in successfully.
# 2024-01-22 08:45:23 DEBUG Attempting to connect to the database.
# 2024-01-22 09:00:45 ERROR Database connection failed.
# 2024-01-22 09:15:10 INFO Data export completed.
# 2024-01-22 10:30:55 WARNING Disk usage above 80%.
# 2024-01-22 11:05:00 DEBUG Starting data backup process.
# 2024-01-22 11:30:15 ERROR Backup process failed.
# 2024-01-22 12:00:00 INFO User logged out.
# 2024-01-22 12:45:05 DEBUG Checking system health.
# 2024-01-22 13:30:30 INFO Scheduled maintenance.



# Вимоги до завдання:

# Скрипт повинен приймати шлях до файлу логів як аргумент командного рядка.
# Скрипт повинен приймати не обов'язковий аргумент командного рядка, після аргументу шляху до файлу логів. Він відповідає за виведення всіх записів певного рівня логування. І приймає значення відповідно до рівня логування файлу. Наприклад аргумент error виведе всі записи рівня ERROR з файлу логів.
# Скрипт має зчитувати і аналізувати лог-файл, підраховуючи кількість записів для кожного рівня логування (INFO, ERROR, DEBUG, WARNING).
# Реалізуйте функцію parse_log_line(line: str) -> dict для парсингу рядків логу.
# Реалізуйте функцію load_logs(file_path: str) -> list для завантаження логів з файлу.
# Реалізуйте функцію filter_logs_by_level(logs: list, level: str) -> list для фільтрації логів за рівнем.
# Реалізуйте функцію count_logs_by_level(logs: list) -> dict для підрахунку записів за рівнем логування.
# Результати мають бути представлені у вигляді таблиці з кількістю записів для кожного рівня. Для цього реалізуйте функцію display_log_counts(counts: dict), яка форматує та виводить результати. Вона приймає результати виконання функції count_logs_by_level.


# Рекомендації для виконання:

# Перш ніж почати, ознайомтеся зі структурою вашого лог-файлу. Зверніть увагу на формат дати та часу, рівні логування INFO, ERROR, DEBUG, WARNING і структуру повідомлень.
# Зрозумійте, як розділені різні компоненти логу, це зазвичай пробіли або спеціальні символи.
# Розділіть ваше завдання на логічні блоки і функції для кращої читабельності і подальшого розширення.
# Парсинг рядка логу виконує ****функцію parse_log_line(line: str) -> dict, яка приймає рядок з логу як вхідний параметр і повертає словник з розібраними компонентами: дата, час, рівень, повідомлення. Використовуйте методи рядків, такі як split(), для розділення рядка на частини.
# Завантаження лог-файлів виконує функція load_logs(file_path: str) -> list, що відкриває файл, читає кожен рядок і застосовує на нього функцію parse_log_line, зберігаючи результати в список.
# Фільтрацію за рівнем логування виконує функція filter_logs_by_level(logs: list, level: str) -> list. Вона дозволить вам отримати всі записи логу для певного рівня логування.
# Підрахунок записів за рівнем логування повинна робити функція count_logs_by_level(logs: list) -> dict, яка проходить по всім записам і підраховує кількість записів для кожного рівня логування.
# Вивід результатів виконайте за допомоги функції display_log_counts(counts: dict), яка форматує та виводить результати підрахунку в читабельній формі.
# Ваш скрипт повинен вміти обробляти різні види помилок, такі як відсутність файлу або помилки при його читанні. Використовуйте блоки try/except для обробки виняткових ситуацій.


# Критерії оцінювання:

# Скрипт виконує всі зазначені вимоги, правильно аналізуючи лог-файли та виводячи інформацію.
# Скрипт коректно обробляє помилки, такі як неправильний формат лог-файлу або відсутність файлу.
# При розробці обов'язково було використано один з елементів функціонального програмування: лямбда-функція, списковий вираз, функція filter, тощо.
# Код добре структурований, зрозумілий і містить коментарі там, де це необхідно.


# Приклад використання:

# При запуску скрипту

# python [main.py](<http://main.py/>) /path/to/logfile.log



# Ми повинні очікувати наступне виведення

# Рівень логування | Кількість
# -----------------|----------
# INFO             | 4
# DEBUG            | 3
# ERROR            | 2
# WARNING          | 1



# Якщо користувач хоче переглянути всі записи певного рівня логування, він може запустити скрипт з додатковим аргументом, наприклад:

# python main.py path/to/logfile.log error



# Це виведе загальну статистику за рівнями, а також детальну інформацію для всіх записів з рівнем ERROR.

# Рівень логування | Кількість
# -----------------|----------
# INFO             | 4
# DEBUG            | 3
# ERROR            | 2
# WARNING          | 1

# Деталі логів для рівня 'ERROR':
# 2024-01-22 09:00:45 - Database connection failed.
# 2024-01-22 11:30:15 - Backup process failed.



