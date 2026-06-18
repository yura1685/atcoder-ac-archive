N = int(input())
a = list(map(int,input().split()))

up = []

l = 0
while l < N:
    r = 0
    count = 0
    while l + r < N-1:
        if a[l+r] < a[l+r+1]:
            count += 1
            r += 1
            if l + r == N-1:
                l = N-1
                if count != 0:
                    up.append(count+1)
        else:
            if count != 0:
                up.append(count+1)
            l += r+1
            break
    if l ==  N-1:
        break

def f(n):
    return n*(n-1)//2

ans = 0
for i in up:
    ans += f(i)

print(ans+N)