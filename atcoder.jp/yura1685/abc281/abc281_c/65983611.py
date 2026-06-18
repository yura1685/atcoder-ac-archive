N, T = map(int,input().split())
A = list(map(int,input().split()))

S = sum(A)
T -= S*(T//S)

playing = 0
while T > 0:
    T -= A[playing]
    playing += 1

T += A[playing-1]
print(playing, T)