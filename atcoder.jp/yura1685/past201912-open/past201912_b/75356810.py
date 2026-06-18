N = int(input())
a1 = int(input())
for _ in range(N-1):
    a2 = int(input())
    if a1 < a2: print('up', a2-a1)
    if a1 == a2: print('stay')
    if a1 > a2: print('down', a1-a2)
    a1 = a2