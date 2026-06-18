N = int(input())
H = list(map(int,input().split()))
stack = []

for h in H:
    print(len(stack))
    while stack and stack[-1] < h:
        stack.pop()
    stack.append(h)