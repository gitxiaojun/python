f = open('D:\\test.txt', 'r', encoding='gbk')
f_new = open('D:\\test1.txt', 'w', encoding='gbk')

for line in f:
    if '��������δ����' in line:
        line = line.replace('��������δ����', '��ѧpython')
    f_new.write(line)
f.close()
f_new.close()