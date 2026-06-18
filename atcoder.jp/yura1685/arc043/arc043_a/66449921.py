N, A, B = map(int,input().split())
S = [int(input()) for _ in range(N)]

if max(S) == min(S):
    print(-1)
    exit()

ave = sum(S)/N

P = B/(max(S)-min(S))
Q = A - P*ave

print(P,Q)