N = int(input())
A = list(map(int,input().split()))

if N % 2 == 1: exit(print('Win'))

xor = 0
for a in A: xor ^= a

print('Win' if xor in A else 'Lose')