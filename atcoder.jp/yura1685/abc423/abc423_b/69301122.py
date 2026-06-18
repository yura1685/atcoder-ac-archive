N = int(input())
L = list(map(int,input().split()))
l, r = -1, -1
for i in range(N):
    if L[i] == 1:
        l = i
        break

for j in range(N-1,-1,-1):
    if L[j] == 1:
        r = j
        break

if l == -1 or l == r:
    print(0)

else:
    print(r-l)