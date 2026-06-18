N = int(input())
A = list(map(int,input().split()))
B = []
cnt = 0
for a in A:
    if a < 0:
        cnt += 1
        a = -a
    if a == 0:
        cnt = -10**18
    B.append(a)
    
if cnt < 0 or cnt % 2 == 0:
    print(sum(B))
else:
    print(sum(B)-2*min(B))