operators = ['+','-','*','/',':']
class MyError(Exception):
    pass

try:
    operator = input('Введите оператор: ')
    first_number = input('Введите первое число: ')
    second_number = input('Введите второе число: ')
    if (operator or first_number or second_number) == ' ':
        raise MyError('Недостаточно данных!')
    assert operator in operators, 'Введён неверный оператор'
    if operator == '+':
        result = first_number + second_number
    elif operator == '-':
        result = first_number - second_number
    elif operator == '/' or ':':
        result = first_number / second_number
    elif operator == '*':
        result = first_number * second_number
except ZeroDivisionError:
    print('На ноль делить нельзя!')
except TypeError:
    print('Введён не тот тип данных!')
except MyError as mr:
    print(mr)
else:
    print(f"Ваш пример: {operator} {first_number} {second_number}")
    print(f"Резултат: {result}")
