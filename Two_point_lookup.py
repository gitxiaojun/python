#二分查找
import random
ue = random.randint(0, 100)
count = 0
while True:
    g = input('Please input nums: ')
    count += 1
    g = int(g)
    if g == ue:
        print('你太聪明了' + str(g))
        break
    elif ue < g:
        print('你猜大了')
    else:
        print('你猜小了')

    if  count >= 5:
        print('你太笨了')
        break