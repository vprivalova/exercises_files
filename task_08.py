f1 = open('input.txt', 'r')

lines = f1.readlines()
result = []

for elem in lines:
    if '100' not in elem:
        result.append(elem)

f1.close()

f2 = open('input.txt', 'w')

for elem2 in result:
    f2.write(elem2)

f2.close()
