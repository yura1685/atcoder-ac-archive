N, M = map(int, input().split())
inf = 3 * 10 ** 5 + 1
item = [set() for _ in range(inf)]
get = [0] * inf
get[1] = 1

for _ in range(M):
    A, B = map(int, input().split())
    item[A].add(B)

now = [1]
while now:
    a = now.pop()
    for b in item[a]:
        if get[b] == 0:
            get[b] = 1
            now.append(b)

print(sum(get))