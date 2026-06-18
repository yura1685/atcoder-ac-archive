N, X, Y = map(int,input().split())
amai = sorted(list(map(int,input().split())), reverse = True)
shoppai = sorted(list(map(int,input().split())),reverse = True)
a, s = 0, 0
for i in range(N):
    a += amai[i]
    if a > X:
        a = i + 1
        break
    if i == N-1 and a <= X:
        a = N
for i in range(N):
    s += shoppai[i]
    if s > Y:
        s = i + 1
        break
    if i == N-1 and s <= Y:
        s = N
print(min(a,s))