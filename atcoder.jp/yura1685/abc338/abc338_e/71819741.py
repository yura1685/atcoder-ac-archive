N = int(input())
s = [0] * (2*N)
for i in range(N):
    A, B = map(int,input().split())
    s[A-1] = i
    s[B-1] = i

S = []
for n in s:
    if S and S[-1] == n: S.pop()
    else: S.append(n)

print('Yes' if S else 'No')