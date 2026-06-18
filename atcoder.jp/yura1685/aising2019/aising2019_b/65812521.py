N = int(input())
A, B = map(int,input().split())
P = list(map(int,input().split()))

easy, medium, hard = 0, 0, 0
for diff in P:
    if diff <= A:
        easy += 1
    elif diff <= B:
        medium += 1
    else:
        hard += 1
print(min(easy, medium, hard))