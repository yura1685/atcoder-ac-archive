def solve():
    A = list(map(int, input().split()))
    d = {}
    for i in range(9):
        d[i+1] = A[i]
    lend = 9 - A.count(0)
    

    if d[5] > 0:
        x = sum(d.values()) - d[5]
        y = d[5]
        if x + 1 >= y:
            print(0)
        else:
            print(y-x-1)
    
    elif lend > 2 or lend < 2:
        print(0)
    
    else:
        for i in range(1,5):
            if d[i] > 0 and d[10-i] > 0:
                print(1)
                break
        else:
            print(0)

for _ in range(int(input())):
    solve()