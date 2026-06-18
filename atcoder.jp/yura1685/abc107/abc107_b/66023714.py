H, W = map(int,input().split())
glid = []
for _ in range(H):
    A = list(input())
    if A != ['.']*W:
        glid.append(A)

l = list(zip(*glid))
l2 = []
for i in l:
    n = len(i)
    if list(i) != ['.']*n:
        l2.append(i)

l3 = list(zip(*l2))
for i in l3:
    print(''.join(i))