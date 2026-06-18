def dis(A, B):
    d = 0
    for i in range(len(A)):
        for j in range(len(A)):
            if A[i][j] != B[i][j]:
                d += 1
    return d

def rotate(A):
    B = list(zip(*A[::-1]))
    return B

N = int(input())
S = [tuple(input()) for _ in range(N)]
T = [tuple(input()) for _ in range(N)]

ans = 100**2

ans = min(ans,dis(S,T))
S = rotate(S)
ans = min(ans,dis(S,T)+1)
S = rotate(S)
ans = min(ans,dis(S,T)+2)
S = rotate(S)
ans = min(ans,dis(S,T)+3)
print(ans)