import os

with open('input.txt', 'r') as f1:
    lines = f1.readlines()

result = []

for index in range(len(lines)):
    if (index + 1) % 2 == 0:
        result.append(lines[index])

os.mkdir('simple')
os.chdir('simple')

with open('output.txt', 'w') as f2:
    for elem in result:
        f2.write(elem)
