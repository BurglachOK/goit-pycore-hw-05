def generator_numbers(text: str):
    for number in text.split():
        try:
            yield float(number)
        except ValueError:
            pass


def sum_profit(text: str):
    total = 0
    for number in generator_numbers(text):
        total += number
    return total


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text)
print(f"Загальний дохід: {total_income}")
# Загальний дохід: 1351.46
