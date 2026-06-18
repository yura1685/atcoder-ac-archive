S = input()
stack = []
for i in range(len(S)):
    if S[i] == '(':
        stack.append(i+1)
    else:
        l = stack.pop()
        r = i + 1
        print(l,r)