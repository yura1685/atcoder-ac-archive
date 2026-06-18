N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
hit, blow = 0, 0
i = 0
while i != len(A):
    if A[i] == B[i]:
        hit += 1
        A.pop(i)
        B.pop(i)
        i -= 1
    i += 1
print(hit)
for j in range(N-hit):
    if A[j] in B:
        blow += 1
print(blow)