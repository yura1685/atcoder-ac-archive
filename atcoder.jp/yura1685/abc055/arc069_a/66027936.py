s, c = map(int,input().split())

if s >= c//2:
    print(c//2)
    exit()

scc = s
c -= 2*s
scc += c//4
print(scc)