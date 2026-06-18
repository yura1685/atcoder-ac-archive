K = int(input())
ans = 0
d = {3:6, 2:3, 1:1}

for a in range(1,K+1):
    for b in range(a,K+1):
        if a*b > K:
            break
        for c in range(b,K+1):
            if a*b*c > K:
                break
            if a*b*c <= K:
                ans += d[len(set([a,b,c]))]
print(ans)