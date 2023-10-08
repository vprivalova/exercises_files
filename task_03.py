f1 = open('input.txt', 'r')
f2 = open('output.txt', 'w')

for line in f1:
    if line[-1] == '\n':
        f2.write(line[-2])
    else:
        f2.write(line[-1])

f1.close()
f2.close()
