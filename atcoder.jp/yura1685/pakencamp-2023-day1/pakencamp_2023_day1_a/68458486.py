from collections import Counter

N = int(input())
A = list(map(int,input().split()))
C = Counter(A)

print('Yes' if min(C.values()) <= 10 else 'No')