N, H = map(int,input().split())
B = []
A = 0
for _ in range(N):
    a, b = map(int,input().split())
    B.append(b)
    A = max(A,a)

B.sort(reverse=True)
ans = 0

for b in B:
    if b > A:
        H -= b
        ans += 1
    else:
        break
    if H <= 0:
        exit(print(ans))

print(ans + (H+A-1)//A)