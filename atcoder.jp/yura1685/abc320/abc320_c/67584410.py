M = int(input())
S1, S2, S3 = [input() for _ in range(3)]
S1, S2, S3 = S1*3, S2*3, S3*3
ans = float('inf')
for i in range(3*M):
    for j in range(3*M):
        if i == j:
            continue
        for k in range(3*M):
            if (k-j)*(k-i) == 0:
                continue
            if S1[i] == S2[j] == S3[k]:
                ans = min(ans, max(i,j,k))

print(ans if ans < float('inf') else -1)