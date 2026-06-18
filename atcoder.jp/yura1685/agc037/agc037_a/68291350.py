S = input()

stack = []
ans = 0
i = 0
while i < len(S):
    s = S[i]
    if stack:
        if s != stack[0]:
            stack.clear()
            stack.append(s)
            i += 1
        else:
            stack.clear()
            if i == len(S)-1:
                ans -= 1
            i += 2
    else:
        stack.append(s)
        i += 1
    ans += 1
print(ans)