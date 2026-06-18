N, K = map(int, input().split())
if N <= 10:
    dp = set([0])
    for _ in range(N):
        dp2 = dp.copy()
        A, B = map(int, input().split())
        for x in dp:
            if x + A <= K:
                dp2.add(x+A)
            if x + B <= K:
                dp2.add(x+B)
        dp = dp2
    print('Yes' if K in dp else 'No')

else:
    M = N // 2
    dp = set([0])
    dpdp = set([0])
    for _ in range(M):
        dp2 = dp.copy()
        a, b = map(int, input().split())
        for x in dp:
            if x + a <= K:
                dp2.add(x+a)
            if x + b <= K:
                dp2.add(x+b)
        dp = dp2
    for _ in range(N-M):
        dpdp2 = dpdp.copy()
        a, b = map(int, input().split())
        for x in dpdp:
            if x + a <= K:
                dpdp2.add(x+a)
            if x + b <= K:
                dpdp2.add(x+b)
        dpdp = dpdp2
    for x in dp:
        if (K-x) in dpdp:
            exit(print('Yes'))
    print('No')