A, B = map(int,input().split())

def ham(s,t):
    s, t = str(s), str(t)
    return (s[0]!=t[0])+(s[1]!=t[1])+(s[2]!=t[2])

ans = A - B
for X in range(100,1000):
    if ham(A,X) == 1:
        ans = max(ans,X-B)
    if ham(B,X) == 1:
        ans = max(ans,A-X)

print(ans)