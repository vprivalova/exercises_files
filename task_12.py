with open('input.txt', 'r') as f1:
    lines = f1.readlines()
    title = lines[0]
    h1 = lines[1]
    p = lines[2:]

with open('index.html', 'w') as f_html:
    f_html.write('<!DOCTYPE html>')
    f_html.write('<html>')
    f_html.write('<head>')
    f_html.write('<title>' + title + '</title>')
    f_html.write('</head>')
    f_html.write('<body>')
    f_html.write('<h1>' + h1 + '</h1>')
    for elem in p:
        f_html.write('<p>' + elem + '</p>')
    f_html.write('</body>')
    f_html.write('</html>')
