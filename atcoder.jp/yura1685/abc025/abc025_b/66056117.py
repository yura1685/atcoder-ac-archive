N, A, B = map(int,input().split())

now = 0
for _ in range(N):
    s, d = map(str,input().split())
    d = int(d)
    if s == 'East':
        if d < A:
            now += A
        elif A <= d <= B:
            now += d
        else:
            now += B
    else:
        if d < A:
            now -= A
        elif A <= d <= B:
            now -= d
        else:
            now -= B
    
if now >= 1:
    print('East', now)
elif now <= -1:
    print('West', -now)
else:
    print(0)