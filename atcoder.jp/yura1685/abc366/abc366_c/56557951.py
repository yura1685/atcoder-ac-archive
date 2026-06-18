from collections import Counter

Q = int(input())
balls = Counter()

for _ in range(Q):
    s = input().strip()
    a = s[0]
    if len(s)>1:
        ball = s[2:]
    if a == '1':
        balls[ball] += 1
    if a == '2':
        if balls[ball] > 0:
            balls[ball] -= 1
            if balls[ball] == 0:
                del balls[ball]
    if a == '3':
        print(len(balls))