N = int(input())
n = N//(2**31)
if n == -1 or n == 0:
    print('Yes')
else:
    print('No')