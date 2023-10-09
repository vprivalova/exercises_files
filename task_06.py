import os.path
f_name = input()

while os.path.isfile(f_name) is False:
    print('Файл не найден. Пожалуйста, попробуйте еще раз')
    f_name = input()

with open(f_name, 'r') as f:
    lines = f.readlines()

num_line = int(input())

while num_line > len(lines):
    print('Строка не найдена. Пожалуйста, попробуйте еще раз')
    num_line = int(input())

print(lines[num_line - 1])
