N, X, Y = map(int,input().split())
bus = []
for _ in range(N-1):
    P, T = map(int,input().split())
    bus.append((P,T))

time = [0] * 840

for s in range(840):
    t = s + X
    for i in range(N-1):
        P, T = bus[i]
        t = (t+P-1)//P*P + T
    t += Y
    time[s] = t

Q = int(input())
for _ in range(Q):
    q = int(input())
    print(time[q % 840] + q//840*840)