f = open('D:\\test.txt', 'r', encoding='gbk')
f_new = open('D:\\test1.txt', 'w', encoding='gbk')

for line in f:
    if '在漫长的未来里' in line:
        line = line.replace('在漫长的未来里', '我学python')
    f_new.write(line)
f.close()
f_new.close()