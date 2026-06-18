def check(x,y):
    if len(x) == len(y):
        dif = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                dif += 1
            if dif >= 2:
                return False
        return True
    if len(x) > len(y):
        x, y = y, x
    for i in range(len(x)):
        if x[i] != y[i]:
            if x[i:] == y[i+1:]:
                return True
            return False
    return True

N, T1 = map(str,input().split())
n = len(T1)
ans = []
for i in range(int(N)):
    s = input()
    if abs(len(s) - n) >= 2:
        continue
    if check(s,T1):
        ans.append(i+1)

print(len(ans))
print(*ans)