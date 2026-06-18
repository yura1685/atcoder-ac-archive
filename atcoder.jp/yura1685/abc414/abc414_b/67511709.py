N = int(input())
ans = ''
L = 0
for _ in range(N):
    c, l = input().split()
    L += int(l)
    if L > 100:
        print('Too Long')
        exit()
    ans += c*int(l)

print(ans)