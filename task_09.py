f1 = open('input.txt', 'r')
f2 = open('output.txt', 'w')

lines = f1.readlines()

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
steps = 0
avg = 0
p_begin = 0
p_end = 0

for i in range(12):
    p_begin = p_end
    p_end = p_end + months[i]

    period = lines[p_begin:p_end]

    for j in range(months[i]):
        steps = steps + int(period[j])

    avg = steps / months[i]
    f2.write(str(round(avg)) + '\n')

    steps = 0
    avg = 0

f1.close()
f2.close()
