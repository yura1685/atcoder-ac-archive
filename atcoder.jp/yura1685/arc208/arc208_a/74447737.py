def solve():
    N = int(input())
    A = list(map(int, input().split()))
    o, x = 0, 0
    for a in A:
        o |= a 
        x ^= a 
    print('Alice' if o - x else 'Bob')

for _ in range(int(input())):
    solve()