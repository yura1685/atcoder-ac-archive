def upshift(glid):
    glid = glid[1:] + [glid[0]]
    return glid

def leftshift(glid):
    for i in range(len(glid)):
        glid[i] = glid[i][1:] + [glid[i][0]]
    return glid

H, W = map(int,input().split())
A = []
B = []
for i in range(H):
    A.append(list(input()))
for i in range(H):
    B.append(list(input()))

for i in range(H):
    for j in range(W):
        if A == B:
            print('Yes')
            exit()
        A = leftshift(A)
    A = upshift(A)
print('No')