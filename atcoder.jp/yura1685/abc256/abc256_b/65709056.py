N = int(input())
A = list(map(int,input().split()))

runner = [0,0,0,0]
for i in range(N):
    if A[i] == 1:
        runner += [1]
    elif A[i] == 2:
        runner += [1,0]
    elif A[i] == 3:
        runner += [1,0,0]
    else:
        runner += [1,0,0,0]

print(sum(runner[:-3]))