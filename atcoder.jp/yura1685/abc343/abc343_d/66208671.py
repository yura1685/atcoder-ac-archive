N, T = map(int,input().split())
player = [0]*(N+1)
point  = {0:N}
dif = 1
for _ in range(T):
    a, b = map(int,input().split())
    p_a = player[a]
    if point[p_a] == 1:
        dif -= 1
    point[p_a] -= 1
    if point.get(p_a+b) == None or point.get(p_a+b) == 0:
        point[p_a+b] = 1
        dif += 1
    else:
        point[p_a+b] += 1
    player[a] += b
    print(dif)