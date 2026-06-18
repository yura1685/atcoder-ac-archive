import bisect

N = int(input())
A = sorted(list(map(int,input().split())))
B = sorted(list(set(A)), reverse = True)
B += [0]*(N-len(B))
for n in B:
    print(bisect.bisect(A,n) - bisect.bisect_left(A,n))