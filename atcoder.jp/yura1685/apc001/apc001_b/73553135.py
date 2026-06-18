N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

cnt1 = cnt2 = 0
for i in range(N):
    a, b = A[i], B[i]
    if a > b:
        cnt2 += a - b 
    if b > a:
        cnt1 += (b - a) // 2

print('Yes' if cnt1 >= cnt2 else 'No')