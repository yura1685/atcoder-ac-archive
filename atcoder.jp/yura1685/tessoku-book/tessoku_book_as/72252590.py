_, C = input().split()
A = input()
n = (A.count('B') - A.count('R')) % 3

if n == 0: X = 'W'
if n == 1: X = 'B'
if n == 2: X = 'R'

print('Yes' if X == C else 'No')