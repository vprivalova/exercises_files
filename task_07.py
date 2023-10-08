f1 = open('input.txt', 'r')
f2 = open('output.txt', 'w')

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
    f2.write(str(division + num3))

f1.close()
f2.close()
