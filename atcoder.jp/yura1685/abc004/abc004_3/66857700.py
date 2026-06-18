N = int(input())
c = [1,2,3,4,5,6]

N %= 30
for i in range(N):
    c[i%5], c[i%5+1] = c[i%5+1], c[i%5]

ans = ''
for x in c:
    ans += str(x)

print(ans)