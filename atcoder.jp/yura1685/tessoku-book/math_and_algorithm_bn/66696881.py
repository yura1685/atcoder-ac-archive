N = int(input())
movie = []
for _ in range(N):
    L, R = map(int,input().split())
    movie.append((R,L))

movie.sort()

last = 0
watch = 0

for R, L in movie:
    if last <= L:
        last = R
        watch += 1

print(watch)