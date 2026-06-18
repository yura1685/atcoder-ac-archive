N, M = map(int,input().split())
s = set()

ans = 0
for _ in range(M):
    R, C = map(int,input().split())
    flag = True
    for i in range(-1,2):
        for j in range(-1,2):
            if (R+i,C+j) in s:
                flag = False
                break
        if not flag:
            break
    if flag:
        s.add((R,C))
        ans += 1

print(ans)