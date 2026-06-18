Q = int(input())
A, B = [], []
for _ in range(Q):
    a, b = map(int,input(). split())
    if a == 1:
        A.append(b)
    elif a == 2:
        B.append(A[-b])
for k in range(len(B)):
    print(B[k])