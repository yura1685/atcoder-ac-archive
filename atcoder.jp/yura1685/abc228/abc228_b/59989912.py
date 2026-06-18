N, X = map(int,input().split())
A = list(map(int,input().split()))
know = [0]*(N+1)
know[X] += 1
while True:
    c = A[X-1]
    if know[c] == 0:
        know[c] += 1
    else:
        break
    X = c
print(sum(know))