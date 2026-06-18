N, K = map(int,input().split())
S = input()
H = []

ha = 0
for i in range(N):
    s = S[i]
    if s == 'L' and i > 0 and S[i-1] == 'L':
        ha += 1
    if s == 'R' and i < N-1 and S[i+1] == 'R':
        ha += 1

print(min(N-1,ha + 2*K))