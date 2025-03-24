import sys
from pathlib import Path


def errors(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            print("Your log file is corrupted")
            sys.exit()
        except KeyError:
            print("Should not appear (KeyError)")
            sys.exit()
        except IndexError:
            print("Should not appear (IndexError)")
            sys.exit()
        except PermissionError:
            print("Please write a real Path")
            sys.exit()
        except FileNotFoundError:
            print("Please provide a real File")
            sys.exit()
    return inner


@errors
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


@errors
def load_logs(file_path: str) -> list:
    return [parse_log_line(line) for line in open(file_path, 'r')]
    # with open(file_path, 'r') as file:
    #     for line in file:
    #         yield parse_log_line(line)


@errors
def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['level'] == level.upper()]
    # for log in logs:
    #     if log['level'] == level:
    #         yield log


@errors
def count_logs_by_level(logs: list) -> dict:
    counts = {}
    for log in logs:
        level = log['level']
        if level in counts:
            counts[level] += 1
        else:
            counts[level] = 1
    return counts 


@errors
def display_log_counts(counts: dict):
    print('Рівень логування | Кількість\n-----------------|----------')
    for level, count in counts.items():
        print(f'{level}'.ljust(17) + f'| {count}')

    if len(sys.argv) == 3:
        filter_logs_by_level(load_logs(Path(sys.argv[1])), sys.argv[2])
        print(f'Деталі логів для рівня \'{sys.argv[2].upper()}\':')
    for level in 





try:
    display_log_counts(count_logs_by_level(load_logs(Path(sys.argv[1]))))
except IndexError:
    print("Please provide a Path")
    sys.exit()


# py log_reader.py ./logfile.log
