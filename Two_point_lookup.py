#���ֲ���
import random
ue = random.randint(0, 100)
count = 0
while True:
    g = input('Please input nums: ')
    count += 1
    g = int(g)
    if g == ue:
        print('��̫������' + str(g))
        break
    elif ue < g:
        print('��´���')
    else:
        print('���С��')

    if  count >= 5:
        print('��̫����')
        break