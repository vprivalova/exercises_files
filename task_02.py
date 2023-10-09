with open('input.txt', 'r') as f1, open('output.txt', 'w') as f2:
    for line in f1:
        if line[0] == 'A':
            f2.write(line)
