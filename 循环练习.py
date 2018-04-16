#!/usr/bin/python
#__*__coding: UTF-8
# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# 程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列
 for i in range(1, 5):
     for j in range(1, 5):
         for k in range(1, 5):
             if (i != k ) and (i != j) and (j != k):
                 print(i, j, k)

# 题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
# 程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。

 i = int(input('净利润:'))
 arr = [1000000,600000,400000,200000,100000,0]
 rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
 r = 0
 for idx in range(0, 6):
     if i > arr[idx]:
         r += (i - arr[idx]) * rat[idx]
         print(i - arr[idx] * rat[idx] )
         i = arr[idx]
 print(r)

# 题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
# 程序分析：
# 假设该数为 x。
# 1、则：x + 100 = n2, x + 100 + 168 = m2
# 2、计算等式：m2 - n2 = (m + n)(m - n) = 168
# 3、设置： m + n = i，m - n = j，i * j =168，i 和 j 至少一个是偶数
# 4、可得： m = (i + j) / 2， n = (i - j) / 2，i 和 j 要么都是偶数，要么都是奇数。
# 5、从 3 和 4 推导可知道，i 与 j 均是大于等于 2 的偶数。
# 6、由于 i * j = 168， j>=2，则 1 < i < 168 / 2 + 1。
# 7、接下来将 i 的所有数字循环计算即可。
 for i in range(1, 85):
     if 168 % i == 0:
         j = 168 / i;
         if i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0:
             m = (i + j) / 2
             n = (i - j) / 2
             x = n * n - 100
             print(x)

# 题目：输入某年某月某日，判断这一天是这一年的第几天？
# 程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：

 year = int(input('year:\n'))
 month = int(input('month:\n'))
 day = int(input('day:\n'))
 months = (0, 31, 59, 120, 151, 181, 212, 243, 173,304, 334)
 if 0 < month <= 12:
     sum = months[month - 1]
 else:
     print('data error')
 print(sum)
 sum += day
 leap = 0
 if (year % 400 == 0) or (year % 4 == 9) and (year % 100 != 0):
     leap = 1
 if (leap == 1) and (month > 2):
     sum += 1
 print('it is the {0} day.'.format(sum))


# 题目：斐波那契数列。
# 程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。

 a,b = 1, 1
 s = int(input('nums:'))
 for i in range(s - 1):
     a, b = b, a + b
     print(a, end=' ')

 n = int(input('nums: '))
 if n == 1:
     print([1])
 if n == 2:
     print([1, 1])
 fibs = [1, 1]
 for i in range(2, n):
     fibs.append(fibs[-1] + fibs[-2])
 print(fibs)
 fe_list = [0, 1]
 for i in range(1,11):
     fe_list.append(sum(fe_list[(i-1):(i+1)]))
 print(fe_list)

 for i in range(1, 10):
     for j in range(1, i+1):
         print('%d * %d = %d' %(i, j, i*j), end='  ')
     print('')

 import time
 my = {1: 'a', 2: 'b'}
 for key, value in my.items():
     print(key, value)
     time.sleep(2)


# 题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
# 程序分析：兔子的规律为数列1,1,2,3,5,8,13,21....
 f1 = 1
 f2 = 1
 for i in range(1, 22):
     print('{0} {1}'.format(f1, f2, end=' '))
     if (i % 3) == 0:
         print('')
     f1 = f1 + f2
     f2 = f1 + f2

# 题目： 获取 100 以内的质数。
# 程序分析：质数（prime number）又称素数，有无限个。质数定义为在大于1的自然数中，除了1和它本身以外不再有其他因数的数称为质数，如：2、3、5、7、11、13、17、19。
 num = []
 i = 2
 for i in range(2, 100):
     j = 2
     for j in range(2, i):
         if (i % j == 0):
             break
     else:
         num.append(i)
 print(num)
























