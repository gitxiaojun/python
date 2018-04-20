f = open('E:\\reboot\\access.txt', 'rt')
count = {}
log = []
for file in f:
    text = file.split(' ')
    log.append(text[0]+ ' '+text[6]+' ' +text[8])

for line in log:
    if line not in count:
        count[line] = 1
    else:
        count[line] += 1
fib = sorted(count.items(), key=lambda items:items[1], reverse=True)[:10]
f.close()
f = open('E:\\reboot\\log', 'wt')
tpl_body = '|{0:^15s}|{1:^50s}|{2:^15s}|{3:^15s}|'
col_title = tpl_body.format('IP', 'URL', 'CODE', 'CNT')
splitline = '-' * len(col_title)
for line in fib:
    print(splitline)
    print(tpl_body.format(line[0].split(' ')[0], line[0].split(' ')[1], line[0].split(' ')[2], str(line[1]))+'\n')
print(splitline)