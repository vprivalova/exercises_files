with open('input.txt', 'r') as f1, open('output.txt', 'w') as f2:
    for line in f1:
        if line[-1] == '\n':
            f2.write(line[-2])
        else:
            f2.write(line[-1])
