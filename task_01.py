with open('input.txt', 'r') as f1:
    result = (f1.read()).upper()

with open('output.txt', 'w') as f2:
    f2.write(result)
