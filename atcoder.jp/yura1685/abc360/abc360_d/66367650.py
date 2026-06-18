from bisect import bisect

N, T = map(int,input().split())
S = input()
X = list(map(int,input().split()))

right = []
left = []

for i in range(N):
    if S[i] == '0':
        left.append(X[i])
    else:
        right.append(X[i])

left.sort()
right.sort()

cross = 0

for ant in right:
    cross += bisect(left,ant+2*T) - bisect(left,ant)

print(cross)