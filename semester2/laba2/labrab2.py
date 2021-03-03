with open('text.txt', mode='r', encoding='utf8') as f1:
    tl = f1.read().split('\n')
    f1.close()

with open('stix.html', mode='r', encoding='utf8') as f2:
    hl = f2.read().split('\n')
    f2.close()

tl.append('</p>')
tl.insert(0, '<p>')

for id, item in enumerate(tl):
    if id == 0 or id == len(tl) - 1:
        hl.insert(hl.index(''), tl[id])
    elif tl[id] != '':
        tl[id] = tl[id] + '<br>'
    elif tl[id] == '':
        tl[id] += '</p><p>'

    hl.insert(hl.index(''), tl[id])


with open('main.html', 'w', encoding='utf8') as out:
    for elm in hl:
        out.write(elm + '\n')

    out.close()