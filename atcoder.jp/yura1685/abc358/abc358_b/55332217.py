N, A = map(int, input(). split())
T = list(map(int, input().split()))
waitingtime = 0
for i in range(len(T)):
    if waitingtime >= T[i]:
        waitingtime += A
        print(waitingtime)
    elif waitingtime < T[i]:
        waitingtime = T[i] + A
        print(waitingtime)