import os.path
f_name = input()
num_line = int(input())

if os.path.isfile(f_name):
    with open(f_name, 'r') as f:
        lines = f.readlines()
    if num_line <= len(lines):
        print(lines[num_line - 1])
    else:
        print('Строка не существует')

else:
    print('Файл не существует')
