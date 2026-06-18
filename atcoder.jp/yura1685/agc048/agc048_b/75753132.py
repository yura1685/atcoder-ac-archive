N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
Od = sorted([A[i] - B[i] for i in range(0, N, 2)], reverse=True)
Ev = sorted([A[i] - B[i] for i in range(1, N, 2)], reverse=True)
ans = sum(B)
for i in range(N//2):
    if Od[i] + Ev[i] > 0: ans += Od[i] + Ev[i]
    else: break
print(ans)