N = int(input())
ans = 0
while N >= 10000:
    N -= 10000
    ans += 1
while N >= 5000:
    N -= 5000
    ans += 1
print(ans + N//1000)