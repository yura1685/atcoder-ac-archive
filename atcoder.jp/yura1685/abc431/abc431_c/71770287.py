N, M, K = map(int,input().split())
H = sorted(map(int,input().split()))
B = sorted(map(int,input().split()))

cnt = 0
b = 0
for h in H:
    while b < M:
        if h <= B[b]:
            b += 1
            cnt += 1
            break
        b += 1

print('Yes' if cnt >= K else 'No')