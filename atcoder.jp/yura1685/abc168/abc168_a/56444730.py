N = int(input())
p = [0,1,6,8]
n = N % 10
if n in p:
    print('pon')
elif n == 3:
    print('bon')
else:
    print('hon')