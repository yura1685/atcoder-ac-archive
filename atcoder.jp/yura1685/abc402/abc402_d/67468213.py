N, M = map(int,input().split())

cnt = [0]*N

for _ in range(M):
    A, B = map(int,input().split())
    cnt[(A+B) % N] += 1

ans = M*(M-1)//2

for i in cnt:
    ans -= i*(i-1)//2

print(ans)