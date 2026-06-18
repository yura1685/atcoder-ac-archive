ans = 0
K = int(input())
for a in range(1,K+1):
    if a**3 > K:
        break
    if K % a == 0:
        X = K//a
        for b in range(a,X+1):
            if b**2 > X:
                break
            if X % b == 0:
                ans += 1

print(ans)