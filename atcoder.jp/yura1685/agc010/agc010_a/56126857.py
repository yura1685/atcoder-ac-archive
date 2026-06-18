#奇数の個数が奇数個だとできない

N = int(input())
A = list(map(int,input().split()))
if sum(A)%2 == 0:
    print('YES')
else:
    print('NO')