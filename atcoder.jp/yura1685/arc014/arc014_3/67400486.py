from collections import deque

N = int(input())
S = input()
d = deque()

for i in range(N):
    s = S[i]
    if not d:
        d.append(s)
    else:
        if d[0] == s:
            d.popleft()
        elif d[-1] == s:
            d.pop()
        else:
            if i == N-1:
                print(len(d)+1)
                exit()
            t = S[i+1]
            if s == t:
                d.append(s)
            elif d[0] == t:
                d.append(s)
            else:
                d.appendleft(s)

print(len(d))