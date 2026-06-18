N = int(input())
A = list(map(int,input().split()))
A.sort()

def read(num):
    c = [0]*(num)
    amari = 0
    for a in A:
        if a <= num and c[a-1] == 0:
            c[a-1] = 1
        else:
            amari += 1
    if c.count(0)*2 <= amari:
        return True
    else:
        return False
    
if N == 1:
    print(int(A[0]==1))
    exit()

l, r = 0, N+1
while (r-l) > 1:
    mid = (r+l)//2
    if read(mid):
        l = mid
    else:
        r = mid

print(l)