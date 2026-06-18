n = int(input())
R = list(map(int,input().split()))
C = list(map(int,input().split()))
q = int(input())
ans = []
for _ in range(q):
    r, c = map(int,input().split())
    r, c = R[r-1], C[c-1]
    ans.append('#' if r + c > n else '.')

print(''.join(ans))