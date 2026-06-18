N, X = map(int,input().split())
jump = {0}
for _ in range(N):
    a, b = map(int,input().split())
    jump2 = set()
    for j in jump:
        if j+a <= X:
            jump2.add(j+a)
        if j+b <= X:
            jump2.add(j+b)
    jump = jump2
    if jump == set():
        print('No')
        exit()
        
if X in jump:
    print('Yes')
else:
    print('No')