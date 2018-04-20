题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
a = int(input('请输入一个数字:\n'))
x = str(a)
flag = True
for i in range(len(x)//2):
    if x[i] != x[-i -1]:
        flag = False
        break
if flag:
    print('%d 是一个回文数!' % a)
else:
    print('%d 不是一个回文数!' % a)
	
	s = ['one', 'two', 'three']
for i in s[::-1]:
    print(i)
	
join练习	
L = [1, 2, 3, 4, 5]
s1 = ','.join(str(n) for n in L)
print(s1)

s1 = '='
sw = ('r', 'w', 'n', 'o','f')
print(s1.join(sw))
