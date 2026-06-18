N = int(input())
A = sorted(list(map(int,input().split())))
M = int(input())
B = list(map(int,input().split()))
L = int(input())
C = list(map(int,input().split()))
Q = int(input())
X = list(map(int,input().split()))

sum_abc = []
for a in A:
    for b in B:
        for c in C:
            sum_abc.append(a+b+c)

d = set(sum_abc)
for x in X:
    if x in d:
        print('Yes')
    else:
        print('No')