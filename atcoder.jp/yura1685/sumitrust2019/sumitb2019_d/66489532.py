N = int(input())
S = input()

ans = 0
for i in range(1000,2000):
    n = str(i)
    a, b, c = n[1], n[2], n[3]
    cnt = 0
    for j in S:
        if j == a and cnt == 0:
            cnt = 1
        elif j == b and cnt == 1:
            cnt = 2
        elif j == c and cnt == 2:
            ans += 1
            break
print(ans)