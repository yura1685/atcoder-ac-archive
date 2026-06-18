N = int(input())
S = input()
if N % 2 == 1:
    print(-1)
else:
    n = N//2
    a = S[:n]
    b = S[n:]
    ans = 0
    for i in range(n):
        if a[i] != b[i]:
            ans += 1
    print(ans)