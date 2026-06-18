def f(n):
    if n == 0:
        return 0
    n = str(n)
    ju = 0
    for i in range(len(n)):
        ju += int(n[i])*8**(len(n)-i-1)
    nine = []
    cnt = 1
    while ju != 0:
        c = ju % (9**cnt)//(9**(cnt-1))
        ju -= c*9**(cnt-1)
        if c == 8:
            c = 5
        nine.append(str(c))
        cnt += 1

    nine = list(reversed(nine))
    return int(''.join(nine))

N, K = map(int,input().split())
for _ in range(K):
    N = f(N)

print(N)