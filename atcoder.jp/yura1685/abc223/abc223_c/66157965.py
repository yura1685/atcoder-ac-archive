N = int(input())
time = 0
length = []
speed  = []
for _ in range(N):
    A, B = map(int,input().split())
    time += A/B
    length.append(A)
    speed.append(B)

t = 0
c = 0
ans = 0
while t < time/2:
    t += length[c]/speed[c]
    ans += length[c]
    c += 1
over = t - time/2
ans -= over*speed[c-1]

print(ans)