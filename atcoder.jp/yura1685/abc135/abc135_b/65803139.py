N = int(input())
p = list(map(int,input().split()))
ans = 0
for i in range(N):
    if p[i] != i+1:
        ans += 1
print('YES' if ans in [0,2] else 'NO')