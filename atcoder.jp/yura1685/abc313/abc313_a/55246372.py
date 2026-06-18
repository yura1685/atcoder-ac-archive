N = int(input())
P = list(map(int, input().split()))
Q = P.pop(0)
if len(P) == 0:
    print(0)
else:
    if Q > max(P):
        print(0)
    elif Q == max(P):
        print(1)
    else:
        print(max(P)-Q+1)