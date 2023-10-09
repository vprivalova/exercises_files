with open('input.txt', 'r') as f1:
    lines = f1.readlines()

result = []

for elem in lines:
    if '100' not in elem:
        result.append(elem)

with open('input.txt', 'w') as f2:
    for elem2 in result:
        f2.write(elem2)
