N = int(input())
A = list(map(int,input().split()))

ans = -float('inf')
for i in range(N):
    taka, aoki = -float('inf'), -float('inf')
    for j in range(N):
        if j == i:
            continue
        if j < i:
            T = A[j:i+1]
        else:
            T = A[i:j+1]
        hoge = sum(T[1::2])
        if aoki < hoge:
            aoki = hoge
            taka = sum(T[::2])
    ans = max(ans,taka)

print(ans)