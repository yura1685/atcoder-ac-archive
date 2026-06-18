A, V = map(int,input().split())
B, W = map(int,input().split())
T = int(input())
if A <= B and (B - A)*(B - A - (V-W)*T) <= 0:
    print('YES')
elif B <= A and (A - B)*(A -B - V*T + W*T) <= 0:
    print('YES')
else:
    print('NO')