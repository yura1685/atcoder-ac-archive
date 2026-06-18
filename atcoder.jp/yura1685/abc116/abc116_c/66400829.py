N = int(input())
h = list(map(int,input().split()))

hoge = [h[0]]
for i in range(1,N):
    hoge.append(h[i]-h[i-1])

ans = 0
for x in hoge:
    if x > 0:
        ans += x

print(ans)