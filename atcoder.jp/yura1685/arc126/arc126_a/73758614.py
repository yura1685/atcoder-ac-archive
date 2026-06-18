def solve():
    ans = 0
    n2, n3, n4 = map(int,input().split())

    n6 = n3 // 2
    use46 = min(n4, n6)
    ans += use46
    n6 -= use46
    n4 -= use46
    use226 = min(n6, n2//2)
    ans += use226
    n6 -= use226
    n2 -= use226 * 2
    use244 = min(n4//2, n2)
    ans += use244
    n4 -= use244 * 2
    n2 -= use244
    if n4 > 0 and n2 >= 3:
        ans += 1
        n4 -= 1
        n2 -= 3
    ans += n2 // 5
    print(ans)

for _ in range(int(input())):
    solve()