N = int(input())
card = []
for i in range(1,N+1):
    A, C = map(int,input().split())
    card.append((A,C,i))

card.sort()
ans = []

hoge = 10**10
for a, c, i in card[::-1]:
    if c < hoge:
        hoge = c
        ans.append(i)
ans.sort()
print(len(ans))
print(*ans)