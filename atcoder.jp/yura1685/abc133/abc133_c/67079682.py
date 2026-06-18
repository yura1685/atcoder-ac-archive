L, R = map(int,input().split())

if L + 2019 <= R:
    print(0)
    exit()

L, R = L % 2019, R % 2019

if L > R:
    print(0)
    exit()

ans = 2019
for i in range(L,R):
    for j in range(i+1,R+1):
        c = (i*j) % 2019
        ans = min(ans,c)

print(ans)