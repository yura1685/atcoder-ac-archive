import itertools

N, M = map(int,input().split())
c = list(itertools.product([0, 1], repeat=N))[1:]
def OR(x,y):
    s = ''
    for i in range(len(x)):
        if x[i] == y[i] == 'x':
            s += 'x'
        else:
            s += 'o'
    return s

store = []
for _ in range(N):
    store.append(input())

ans = 10
for pick in c:
    check = []
    for i in range(N):
        if pick[i] == 1:
            check.append(store[i])
    x = check[0]
    check = check[1:]
    for i in range(len(check)):
        x = OR(x,check[i])
    if x == 'o'*M:
        ans = min(ans,sum(pick))

print(ans)