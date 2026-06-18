N, M = map(int,input().split())
A = list(map(int,input().split()))
S = sum(A)
flag = 0
for a in A:
    if S - a == M:
        flag = 1

print('Yes' if flag else 'No')