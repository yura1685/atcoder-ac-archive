N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

a, b, c = [0]*46, [0]*46, [0]*46
for i in range(N):
    a[A[i] % 46] += 1
    b[B[i] % 46] += 1
    c[C[i] % 46] += 1

ans = 0
for i in range(46):
    for j in range(46):
        x, y = a[i], b[j]
        n = (i+j)%46
        z = c[-n]
        ans += x*y*z
        
print(ans)