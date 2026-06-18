from collections import Counter

N = int(input())
A = list(map(int,input().split()))
m, M = min(A), max(A)
C = Counter(A)

# M or m + M に限る

flag = True
for c in C.keys():
    if c == M:
        continue
    if 2*c == M:
        if C[c] % 2 == 1:
            flag = False
            break
    if C[c] != C[M-c]:
        flag = False
        break

if flag:
    print(M, end=' ')

flag = True
for c in C.keys():
    if 2*c == m+M:
        if C[c] % 2 == 1:
            flag = False
            break
    if C[c] != C[M+m-c]:
        flag = False
        break

if flag:
    print(M+m)