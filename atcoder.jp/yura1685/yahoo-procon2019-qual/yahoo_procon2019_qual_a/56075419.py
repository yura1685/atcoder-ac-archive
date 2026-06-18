N, K = map(int,input().split())
n = N // 2 + N % 2
if n >= K:
    print('YES')
else:
    print('NO')