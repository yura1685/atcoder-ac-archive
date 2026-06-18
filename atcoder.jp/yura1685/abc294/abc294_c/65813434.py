import bisect

N, M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = sorted(A+B)

ans_A = []
ans_B = []
for a in A:
    ans_A.append(bisect.bisect(C,a))
for b in B:
    ans_B.append(bisect.bisect(C,b))


print(*ans_A)
print(*ans_B)