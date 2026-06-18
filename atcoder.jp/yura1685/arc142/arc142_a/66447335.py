N, K = map(int,input().split())

def rev(n):
    l = list(str(n))
    l.reverse()
    return int(''.join(l))

if K % 10 == 0 or rev(K) < K:
    print(0)
    exit()

ans = set()
c = K
while c <= N:
    ans.add(c)
    c *= 10

c = rev(K)
while c <= N:
    ans.add(c)
    c *= 10

print(len(ans))