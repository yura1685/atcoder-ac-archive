Q = int(input())
stack = []
score = 0
ind = -1
for i in range(Q):
    query = input().split()
    if query[0] == '1':
        c = query[1]
        stack.append(c)
        if c == '(':
            score += 1
        else:
            score -= 1
            if ind == -1 and score < 0:
                ind = len(stack)
    else:
        c = stack.pop()
        if c == '(':
            score -= 1
        else:
            score += 1
            if ind >= 0 and len(stack) == ind-1:
                ind = -1
    print('Yes' if (score == 0 and ind == -1) else 'No')