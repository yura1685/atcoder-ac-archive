N, K = map(int,input().split())

friend = []
for _ in range(N):
    a, b = map(int,input().split())
    friend.append((a,b))
friend.sort()

vil = 0
money = K
for i in range(N):
    a, b = friend[i]
    if vil + money < a:
        break
    else:
        money += b - a + vil
        vil = a
print(vil+money)