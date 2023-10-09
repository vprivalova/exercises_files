with open('input.txt', 'r') as f1:
    lines = f1.readlines()

result = []

for elem in lines:
    result.append(int(elem))

result.sort(reverse=True)

with open('output.txt', 'w') as f2:
    for elem2 in result:
        f2.write(str(elem2) + '\n')
