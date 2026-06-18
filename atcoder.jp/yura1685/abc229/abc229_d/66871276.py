S = input()
K = int(input())

if len(S) <= K:
    print(len(S))
    exit()

def xxx(n):   #長さnを達成可能か？
    c = S[:n]
    dot = c.count('.')
    if dot <= K:
        return True
    for i in range(len(S)-n):
        if S[i] == '.':
            dot -= 1
        if S[n+i] == '.':
            dot += 1
        if dot <= K:
            return True
    return False

l, r = 0, len(S) + 1
while (r-l) > 1:
    mid = (l+r)//2
    if xxx(mid):
        l = mid
    else:
        r = mid

print(l)