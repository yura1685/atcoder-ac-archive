N = int(input())
L = list(map(int, input().split()))
ans = 0
for i in range(2*N-2):
    if L[i] == L[i+2]:
        ans += 1
print(ans)