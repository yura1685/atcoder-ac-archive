P, Q = map(int,input().split())
A, B = map(int,input().split())
if P >= Q:
    print(A*Q)
else:
    print(A*P+B*(Q-P))