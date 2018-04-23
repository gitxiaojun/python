ng = {}
path = 'E:\\access.txt'
with open(path) as f:
    for line in f:
        node = line.split()
        key = (node[0], node[6], node[8])
        ng[key] = ng.get(key, 0) + 1
stat_list = list(ng.items())

for j in range(10):
    for i in range(len(stat_list) - 1):
        if stat_list[i][1] > stat_list[i + 1][1]:
            stat_list[i], stat_list[i + 1] = stat_list[i + 1], stat_list[i]

sa = '|{ip:20s}|{url:50s}|{code:5s}|{count:10d}|\n'
with open(path, 'a+') as f:
    for key, value in stat_list[-1:-11:-1]:
        print('|{ip:20s}|{url:45s}|{code:5s}|{count:10d}|\n'.format(ip=key[0], url=key[1], code=key[2], count=value))