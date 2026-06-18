X, N = map(int,input().split())
p = list(map(int,input().split()))

i = 0
while True:
    if X - i not in p:
        print(X-i)
        break
    if X + i not in p:
        print(X+i)
        break
    i += 1