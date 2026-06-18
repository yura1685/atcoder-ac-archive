Q, H, S, D = map(int,input().split())
N = int(input())
L1 = min(4*Q, 2*H, S)

tea = 0
if N % 2 == 1:
    tea += L1

L2 = min(D, 2*L1)
tea += (N//2)*L2

print(tea)