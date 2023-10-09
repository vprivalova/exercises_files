with open('input.txt', 'r') as f1:
    numbers = f1.readlines()

try:
    num1 = int(numbers[0])
    num2 = int(numbers[1])
    num3 = int(numbers[2])
    division = num1 / num2

except ZeroDivisionError:
    print('Значение выражения не может быть определено в связи с делением на ноль')

except ValueError:
    print('Входные данные должны быть целыми числами')

else:
    with open('output.txt', 'w') as f2:
        f2.write(str(division + num3))
