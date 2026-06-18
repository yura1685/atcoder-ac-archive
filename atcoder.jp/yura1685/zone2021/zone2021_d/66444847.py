from collections import deque

S = input()
ans = deque()
rev = 0

for s in S:
    if s == 'R':
        rev = 1-rev
    else:
        if not rev:
            if ans and ans[-1] == s:
                ans.pop()
            else:
                ans.append(s)
        else:
            if ans and ans[0] == s:
                ans.popleft()
            else:
                ans.appendleft(s)

c = list(ans)
if rev:
    c.reverse()
print(''.join(c))