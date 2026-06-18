def sq(x): return x * x

def solve():
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    print('Yes' if sq(r1-r2) <= sq(x2-x1) + sq(y2-y1) <= sq(r1+r2) else 'No')
    
T = int(input())
for _ in range(T):
    solve()