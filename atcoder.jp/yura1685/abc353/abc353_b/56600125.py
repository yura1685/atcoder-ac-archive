N, K = map(int,input().split())
A = list(map(int,input().split()))
time = 0
while len(A) != 0:
    ride = 0
    while ride < K:
        ride += A[0]
        if ride <= K:
            A.pop(0)
        elif ride > K:
            ride -= A[0]
            break
        if len(A) == 0:
            break
    time += 1
print(time)