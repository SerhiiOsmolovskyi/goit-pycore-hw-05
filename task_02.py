import re
from typing import Callable

def generator_numbers(text: str):

    pattern = r'\b\d+\.\d{2}\b|\b\d+\b'
    for match in re.finditer(pattern, text):
        yield float(match.group())  # Повертаємо числа як float

def sum_profit(text: str, func: Callable):
    return sum(func(text))

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income:.2f}") # Загальний дохід: 1351.46
