from sortedcontainers import SortedList

N = int(input())
S = input()
L = SortedList()

for i in range(N):
    if S[i] != 'R':
        continue
    l, r = 0, 0
    for j in range(i-1,-1,-1):
        if S[j] == 'A':
            l += 1
        else:
            break
    for j in range(i+1, N):
        if S[j] == 'C':
            r += 1
        else:
            break
    if min(l,r) > 0:
        L.add(min(l,r))

for i in range(16851685):
    if not L:
        print(i)
        break
    if i % 2 == 0:
        u = L.pop()
        if u > 1:
            L.add(u-1)
    else:
        L.pop(0)