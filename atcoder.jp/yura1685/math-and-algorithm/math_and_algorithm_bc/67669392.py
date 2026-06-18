N, K = map(int,input().split())
A = [abs(int(x)) for x in input().split()]
S = sum(A)

if S <= K and (S-K) % 2 == 0:
    print('Yes')
else:
    print('No')