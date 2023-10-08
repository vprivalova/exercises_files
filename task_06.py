import os.path
f_name = input()

while os.path.isfile(f_name) is False:
    print('File is not found. Please, try again')
    f_name = input()

f = open(f_name, 'r')
lines = f.readlines()

num_line = int(input())

while num_line > len(lines):
    print('This line does not exist. Please, try again')
    num_line = int(input())

print(lines[num_line - 1])

f.close()
