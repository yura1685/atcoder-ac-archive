N, M = map(int,input().split())
Ta = set(input())
Ao = set(input())

Q = int(input())
for _ in range(Q):
    W = input()
    ans = 0
    if all([w in Ta for w in W]):
        ans += 1
    if all([w in Ao for w in W]):
        ans += 2
    print(['Unknown', 'Takahashi', 'Aoki'][ans % 3])