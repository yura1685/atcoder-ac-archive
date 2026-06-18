N = int(input())
A = []
B = []
for _ in range(N):
    a = str(input())
    if a[0] == '!':
        A.append(a[1:])
    else:
        B.append(a)

A = set(A)
B = set(B)
if len(A) <= len(B):
    for i in A:
        if i in B:
            print(i)
            exit()
if len(A) > len(B):
    for i in B:
        if i in A:
            print(i)
            exit()
print('satisfiable')