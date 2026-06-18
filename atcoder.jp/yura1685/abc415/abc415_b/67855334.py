S = input()

cnt = 0
ans = ""
for i in range(len(S)):
    s = S[i]
    if s == "#" and cnt:
        ans += str(i+1)
        print(ans)
        cnt = 0
        ans = ""
    elif s == "#":
        ans += str(i+1) + ","
        cnt += 1