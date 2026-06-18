N = int(input())
a, b, c = map(int,input().split())
dpA = [a]
dpB = [b]
dpC = [c]
for _ in range(N-1):
    a, b, c = map(int,input().split())
    apA = a+max(dpB[-1],dpC[-1])
    apB = b+max(dpA[-1],dpC[-1])
    apC = c+max(dpA[-1],dpB[-1])
    dpA.append(apA)
    dpB.append(apB)
    dpC.append(apC)

print(max(dpA[-1],dpB[-1],dpC[-1]))