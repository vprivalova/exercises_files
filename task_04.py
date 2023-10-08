import os.path
f_name = input()
num_line = int(input())

if os.path.isfile(f_name):
    f = open(f_name, 'r')
    lines = f.readlines()
    if num_line <= len(lines):
        print(lines[num_line - 1])
    else:
        print('This line does not exist')

    f.close()

else:
    print('File is not found')
