def comb11(n):
    ans = 1
    for i in range(11):
        ans *= n-1-i
    ans //= (1*2*3*4*5*6*7*8*9*10*11)
    return ans

L = int(input())
print(comb11(L))