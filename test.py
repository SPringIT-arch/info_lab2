num = '123456789ABCDEF'
n = 4
ln = len(num)

for n in range(n):
    flag = 0
    for i in range(2**n, ln + 1, 2**(n+1)):
        print([j for j in num[i - 1 : i + 2**n - 1]])
