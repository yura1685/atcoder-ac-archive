N = int(input())
A = list(map(int,input().split()))[:8]

if N < 8:
    ans = [set() for _ in range(200)]
    for n in range(1<<N):
        cnt = 0
        s = set()
        for i in range(N):
            if (n >> i) & 1:
                cnt += A[i]
                s.add(i+1)
        cnt %= 200
        if ans[cnt]:
            print('Yes')
            print(len(ans[cnt]), *ans[cnt])
            print(len(s), *s)
            exit()
        else:
            ans[cnt] = s

else:
    ans = [set() for _ in range(200)]
    for n in range(1<<8):
        cnt = 0
        s = set()
        for i in range(8):
            if (n >> i) & 1:
                cnt += A[i]
                s.add(i+1)
        cnt %= 200
        if ans[cnt]:
            print('Yes')
            print(len(ans[cnt]), *ans[cnt])
            print(len(s), *s)
            exit()
        else:
            ans[cnt] = s

print('No')