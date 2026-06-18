def c(n):
    return n*(n-1)//2

N = int(input())
S = input()
ans = 0

now = 0
while now < N:
    count = 1
    moji = S[now+count-1]
    while now + count < N:
        if S[now+count] != moji:
            break
        count += 1
    ans += c(count)
    now += count
print(ans)