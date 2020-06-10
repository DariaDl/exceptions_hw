operators = ['+','-','*','/',':']
class MyError(Exception):
    pass

try:
    print('Введите пример в следующем виде: + 2 2')
    primer = str(input('Введите пример: '))
    list = primer.split(' ')
    operator = list[0]
    first_number = int(list[1])
    second_number = int(list[2])
    if (operator or first_number or second_number) == ' ':
        raise MyError('Недостаточно данных!')
    assert operator in operators, 'Введён неверный оператор'
    if operator == '+':
        result = first_number + second_number
    elif operator == '-':
        result = first_number - second_number
    elif (operator == '/') or (operator == ':'):
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
