N = int(input())
pue = 100
for a in range(1,N):
    ans = 0
    B = list(str(N-a))
    A = list(str(a))
    for i in range(len(A)):
        ans += int(A[i])
    for j in range(len(B)):
        ans += int(B[j])
    pue = min(ans,pue)
print(pue)