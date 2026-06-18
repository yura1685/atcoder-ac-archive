N = int(input())
A = list(map(int,input().split()))

bit = 0
for a in A:
    bit ^= a

for a in A:
    print(bit^a, end=' ')