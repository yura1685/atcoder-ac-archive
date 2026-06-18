N, T, P = map(int,input().split())
L = list(map(int,input().split()))
day = 0
while True:
    human = 0
    for i in range(N):
        if L[i] >= T:
            human += 1
    if human >= P:
        print(day)
        exit()
    else:
        day += 1
        for i in range(N):
            L[i] += 1 