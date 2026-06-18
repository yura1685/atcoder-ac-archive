def renzoku(n):
    return n*(n-1)//2

N = int(input())
A = list(map(int,input().split()))
B = []
for i in range(N-1):
    B.append(A[i+1]-A[i])

ans = 2*N-1

a, counter = 0, 0
while True:
    if a >= N-1:
        break
    c = B[a]
    while B[a+counter] == c:
        counter += 1
        if a + counter == N-1:
            break
    ans += renzoku(counter)
    a += counter
    counter = 0
print(ans)