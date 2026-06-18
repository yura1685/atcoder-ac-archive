N, K = map(int,input().split())
H = []
for _ in range(N):
    H.append(int(input()))
H = sorted(H)

now_min = 10**9
for i in range(N-K+1):
    h_h = H[i+K-1] - H[i]
    now_min = min(h_h,now_min)
print(now_min)