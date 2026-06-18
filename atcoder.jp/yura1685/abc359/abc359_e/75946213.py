N = int(input())
H = list(map(int, input().split()))
stack = []
ans = 0
for i, h in enumerate(H):
    w = 1
    while stack and stack[-1][0] <= h:
        w += stack[-1][1]
        ans -= stack[-1][0] * stack[-1][1]
        stack.pop()
    ans += h * w
    stack.append((h, w))
    print(ans + 1)