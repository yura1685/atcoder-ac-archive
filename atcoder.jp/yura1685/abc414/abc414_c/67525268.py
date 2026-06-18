A = int(input())
N = int(input())

def Xsinsuu(n, X):
    ans = ''
    while n > 0:
        ans = str(n % X) + ans
        n //= X
    return ans or "0"

ans = 0

for i in range(1,10**6):
    s = str(i)
    kisu = int(s + s[-2::-1])
    if kisu > N:
        break
    XXX = Xsinsuu(kisu, A)
    if XXX == XXX[::-1]:
        ans += kisu
    gusu = int(s + s[::-1])
    YYY = Xsinsuu(gusu, A)
    if gusu <= N and YYY == YYY[::-1]:
        ans += gusu

print(ans)