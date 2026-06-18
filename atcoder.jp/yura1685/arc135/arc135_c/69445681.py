N = int(input())
A = list(map(int,input().split()))
B = ['0b0']

cnt = [0] * 30
for a in A:
    b = bin(a)
    B.append(b)
    for i in range(len(b)-2):
        cnt[i] += int(b[-1-i])

ans = 0
for b in B:
    res = 0
    n = len(b)
    for i in range(30):
        if i <= n - 3:
            bit = int(b[-1-i])
            if bit == 0:
                res += cnt[i] * 2**i
            else:
                res += (N-cnt[i]) * 2**i
        else:
            res += cnt[i] * 2**i
    ans = max(ans,res)

print(ans)