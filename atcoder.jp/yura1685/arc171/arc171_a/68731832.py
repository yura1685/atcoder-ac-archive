def solve():
    N, A, B = map(int,input().split())
    if A > N:
        res = 'No'
    elif A == N:
        if B > 0:
            res = 'No'
        else:
            res = 'Yes'
    else:
        if B <= (N-A)*min((N+1)//2,N-A):
            res = 'Yes'
        else:
            res = 'No'
    print(res)

for _ in range(int(input())):
    solve()