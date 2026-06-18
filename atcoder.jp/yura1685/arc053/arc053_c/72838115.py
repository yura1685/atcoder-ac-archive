N = int(input())
C1, C2 = [], []
for _ in range(N):
    a, b = map(int,input().split())
    [C1, C2][a>=b].append((a,b))
C1.sort(key= lambda x:x[0])
C2.sort(key= lambda x:x[1], reverse=True)

C1 += C2

C = 0
ans = 0
for a, b in C1:
    C += a
    ans = max(ans, C)
    C -= b

print(ans)