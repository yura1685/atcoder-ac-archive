from math import gcd

N, K = map(int, input().split())
A = list(map(int, input().split()))
G = gcd(*A)
print('POSSIBLE' if K % G == 0 and K <= max(A) else 'IMPOSSIBLE')