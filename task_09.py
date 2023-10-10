# import random
# with open('input.txt', 'w') as f1:
#     for i in range(365):
#         f1.write(str(random.randint(100, 30000))+'\n')


with open('input.txt', 'r') as f1:
    lines = f1.readlines()

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
steps = 0
avg = 0
p_begin = 0
p_end = 0

with open('output.txt', 'w') as f2:
    for index in range(12):
        p_begin = p_end
        p_end = p_end + months[index]

        period = lines[p_begin:p_end]

        for index2 in range(months[index]):
            steps = steps + int(period[index2])

        avg = steps / months[index]
        f2.write(str(round(avg)) + '\n')

        steps = 0
        avg = 0
