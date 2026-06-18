N = int(input())
A = list(map(int,input().split()))

X0 = [0]*61
X1 = [0]*61

for a in A:
    b = bin(a)[2:]
    b = '0'*(61-len(b)) + b
    for i in range(61):
        if b[i] == '0':
            X0[i] += 1
        else:
            X1[i] += 1

ans = 0
mod = 10**9 + 7

for i in range(61):
    ans += X0[-i-1] * X1[-i-1] * pow(2,i,mod) % mod

print(ans % mod)