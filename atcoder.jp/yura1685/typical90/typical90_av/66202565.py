N, K = map(int,input().split())
hoge = []
for _ in range(N):
    a, b = map(int,input().split())
    hoge.append(b)
    hoge.append(a-b)

hoge.sort(reverse=True)
print(sum(hoge[:K]))