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


# 题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
# 程序分析：程序分析：(a>b)?a:b这是条件运算符的基本例子。

 score = int(input('输入分数:\n'))
 if score >= 90:
     grade = 'A'
 elif score >= 60:
     grade = 'B'
 else:
     grade = 'C'
 print('{0} 属于 {1}'.format(score, grade))


# 题目：猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。

 x2 = 1
 for  day in range(9, 0, -1):
     x1 = (x2 + 1) * 2
     x2 = x1
 print(x1)

# 题目：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
 for i in range(ord('x'), ord('z') + 1):
     for j in range(ord('x'), ord('z') + 1):
         if i != j:
             for k in range(ord('x'), ord('z') + 1):
                 if (i != k ) and (j != k):
                     if (i != ord('x')) and (k != ord('x')) and (k != ord('z')):
                         print('order is a--%s\t b--%s\t c--%s' %(chr(i), chr(j), chr(k)))

# 题目：打印出如下图案（菱形）:
#  *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

# 程序分析：先把图形分成两部分来看待，前四行一个规律，后三行一个规律，利用双重for循环，第一层控制行，第二层控制列。
# 程序源代码：

 from sys import stdout
 for i in range(4):
     for j in range(2 - i + 1):
         stdout.write(' ')
     for k in range( 2 * i + 1):
         stdout.write('*')
     print('')
 for i in range(3):
     for j in range(i + 1):
         stdout.write(' ')
     for k in range(4 - 2 * i + 1):
         stdout.write('*')
     print('')


# 题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
# 程序分析：请抓住分子与分母的变化规律。

 a = 2
 b = 1
 s = 0
 for n in range(1, 21):
     s += a / b
     t = a
     a = a + b
     b = t
 print(s)

# 题目：求1+2!+3!+...+20!的和。
# 程序分析：此程序只是把累加变成了累乘。
 n = 0
 s = 0
 t = 1
 for n in range(1, 21):
     t *= n
     s += t
 print('1! + 2! + 3! + ... + 20! = %d' % s)