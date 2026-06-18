A, B, X = map(int,input().split())

ans = 0
for i in range(1,100):
    p = B*i
    if X < p:
        break
    Y = (X-p)//A #Y円でA*Nを買いたい
    if Y < 10**(i-1):
        continue
    else:
        ans = max(ans,min(Y,10**i-1))

print(min(ans,10**9))