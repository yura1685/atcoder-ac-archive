N, K = map(int,input().split())
ans = [K // (2**N)] * (2**N)
K %= 2**N
for i in range(K):
    ans[(2**N*i)//K] += 1
print(1 if K else 0)
print(*ans)