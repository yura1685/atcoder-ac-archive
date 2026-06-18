N, a = map(int, input().split())
a -= 1
k = input()
b = [int(x) - 1 for x in input().split()]

step = [-1] * N
step[a] = 0
now = a
for i in range(N+10):
    nxt = b[now]
    if step[nxt] == -1:
        step[nxt] = step[now] + 1
        now = nxt
    else:
        cycle = step[now] + 1 - step[nxt]
        break
T, C = step[nxt], cycle

if len(k) <= 6 and int(k) < T:
    move = int(k)
else:
    mod = 0
    for n in k:
        mod = (10 * mod + int(n)) % C
    move = T + (mod - T) % C

now = a
for _ in range(move):
    now = b[now]
print(now + 1)