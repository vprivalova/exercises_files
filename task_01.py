f1 = open('input.txt', 'r')
f2 = open('output.txt', 'w')

f2.write((f1.read()).upper())

f1.close()
f2.close()
