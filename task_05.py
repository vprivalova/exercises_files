import os.path
f_name = input()

while os.path.isfile(f_name) is False:
    print('Файл не найден. Пожалуйста, попробуйте еще раз')
    f_name = input()

f = open(f_name, 'r')
lines = f.readlines()

num_line = int(input())

if num_line <= len(lines):
    print(lines[num_line - 1])
else:
    print('Строка не существует')

f.close()
