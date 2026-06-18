from collections import deque

def solve(): 
    N, D = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    dq = deque()
    ans = sum(A) - sum(B)
    for day in range(N):
        # morning
        dq.append((A[day], day))
        # noon
        use = B[day]
        while True:
            egg, d = dq.popleft()
            if use - egg <= 0:
                if use - egg < 0:
                    dq.appendleft((egg-use, d))
                break
            use -= egg
        # night
        while dq:
            egg, d = dq.popleft()
            if d + D > day:
                dq.appendleft((egg, d))
                break
            ans -= egg
    print(ans)

for _ in range(int(input())):
    solve()