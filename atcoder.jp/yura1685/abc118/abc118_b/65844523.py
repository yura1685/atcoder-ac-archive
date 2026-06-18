N, M = map(int,input().split())
food = [0]*(M+1)
for _ in range(N):
    K = list(map(int,input().split()))
    Af = K[1:]
    for i in Af:
        food[i] += 1
print(food.count(N))