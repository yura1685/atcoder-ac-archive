A = list(map(int,input().split()))
B = []
c = 0
for i in range(1,14):
    B.append(A.count(i))
for i in range(13):
    if B[i] >= 2:
        c += 1
if c >= 2 and max(B) >= 3:
    print('Yes')
else:
    print('No')