#ABC355-C "Bingo 2"

N, T = map(int,input().split())
A = list(map(int,input().split()))

yoko = [0] * N
tate = [0] * N
naname = [0,0]

time = 1
for i in range(T):
    x = A[i]
    t, y = (x % N - 1) % N, (x-1) // N
    yoko[y] += 1
    tate[t] += 1
    if y == t:
        naname[0] += 1
    if y + t == N - 1:
        naname[1] += 1
    if yoko[y] == N or tate[t] == N or max(naname) == N:
        print(time)
        exit()
    time += 1
print(-1)