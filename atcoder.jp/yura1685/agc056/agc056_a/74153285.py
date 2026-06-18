N = int(input())
S = [['.'] * N for _ in range(N)]
idx = 0
for i in range(N):
    S[i][idx] = S[i][(idx+1)%N] = S[i][(idx+2)%N] = '#'
    idx = (idx + 3) % N
if N % 3:
    S[0], S[N//3-1] = S[N//3-1], S[0]
    S[N-N//3], S[N-1] = S[N-1], S[N-N//3]
for s in S: print(''.join(s))