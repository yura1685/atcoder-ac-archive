N, K, M, R = map(int,input().split())

score = [int(input()) for _ in range(N-1)]
score.sort(reverse=True)

if K < N:
    S = sum(score[:K])
    if S >= R*K:
        print(0)
        exit()

S = sum(score[:K-1])
X = K*R - S
if X > M:
    print(-1)
else:
    print(max(X,0))