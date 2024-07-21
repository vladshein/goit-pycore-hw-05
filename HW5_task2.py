#HW5_task2
import re

#define a generator to find real numbers in a string
def generator_numbers(text: str):
    #create the re object with requested pattern
    pattern = re.compile(r'-?\d+\.?\d*')
    
    #find all occurences and yield matches by one
    for match in pattern.finditer(text):
        yield float(match.group())

#define resultant function that will calculate total number
def sum_profit(text: str, func: callable):
    total = 0

    for number in generator_numbers(text):
        total += number

    return total

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(total_income)