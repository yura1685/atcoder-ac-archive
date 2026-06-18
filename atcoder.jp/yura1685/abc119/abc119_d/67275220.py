from bisect import bisect

A, B, Q = map(int,input().split())
shri = [-float('inf')]
temp = [-float('inf')]

for _ in range(A):
    shri.append(int(input()))
for _ in range(B):
    temp.append(int(input()))
shri.append(float('inf'))
temp.append(float('inf'))

for _ in range(Q):
    x = int(input())
    Sl, Sr = x - shri[bisect(shri,x)-1], shri[bisect(shri,x)] - x
    Tl, Tr = x - temp[bisect(temp,x)-1], temp[bisect(temp,x)] - x
    print(min(max(Sr,Tr),max(Sl,Tl),Sl+Tr+min(Sl,Tr),Sr+Tl+min(Sr,Tl)))