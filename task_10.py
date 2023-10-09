import os

with open('input.txt', 'r') as f1:
    lines = f1.readlines()

result = []

for i in range(len(lines)):
    if (i + 1) % 2 == 0:
        result.append(lines[i])

os.mkdir('simple')
os.chdir('simple')

with open('output.txt', 'w') as f2:
    for elem in result:
        f2.write(elem)
