# 要はN!! = (N/2)! * 2^yura
N = int(input())
if N % 2 == 1:
    print(0)
    exit()
N //= 2

def rujandoru(n):
    ans = 0
    for i in range(1,32):
        ans += n//(5**i)
    return ans

print(rujandoru(N))