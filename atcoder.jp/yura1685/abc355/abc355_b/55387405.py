N, M = map(int, input(). split())
A = list(map(int, input(). split()))
B = list(map(int, input(). split()))
l = N + M
A += [201] * 100
B += [201] * 100
c = 1
for i in range(l):
    if min(A) < min(B):
        A.remove(min(A))
        if c == 0:
            print('Yes')
            exit()
        c = 0
    elif min(A) > min(B):
        B.remove(min(B))
        c = 1
print('No')