N, K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

x = y = True

for i in range(1,N):
    x1 = (x and abs(A[i]-A[i-1]) <= K) or (y and abs(A[i]-B[i-1]) <= K)
    y1 = (y and abs(B[i]-B[i-1]) <= K) or (x and abs(B[i]-A[i-1]) <= K)
    x, y = x1, y1

print('Yes' if x or y else 'No')