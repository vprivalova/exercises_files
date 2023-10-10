with open('input.txt', 'r') as f1:
    text = f1.read().split()

signs = '!/.,:-?;'
text_clear = []
frequency = {}

for word in text:
    if word not in signs:
        if word[-1] in signs:
            text_clear.append(word[:(len(word) - 1)].lower())
        else:
            text_clear.append(word.lower())

for elem in text_clear:
    if frequency.get(elem, 0) == 0:
        frequency[elem] = 1
    else:
        frequency[elem] = frequency[elem] + 1

result_words = []

for r_key in frequency:
    result_words.append(r_key)

result_words.sort()

with open('output.txt', 'w') as f2:
    for result in result_words:
        f2.write(result + ' - частота вхождений: ' + str(frequency[result]) + '\n')
