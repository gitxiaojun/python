jobs = []
while True:
    prom = input('�������κ�����/do: ')
    if prom == 'do':
        if jobs:
            print('���������:' + jobs.pop(0))
        else:
            print('�����Ѿ�����ˣ����Է����°��ˡ�')
            break
    else:
        jobs.append(prom)