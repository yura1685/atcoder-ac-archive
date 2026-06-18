N, A, B, C, D = map(int,input().split())
S = input()

if A < C < B:
    if '##' not in S[A:C] and '##' not in S[B:D]:
        print('Yes')
    else:
        print('No')
elif B < C < D:
    if '##' not in S[A:D]:
        print('Yes')
    else:
        print('No')
else:
    if '##' not in S[A:C] and '...' in S[B-2:D+1]:
        print('Yes')
    else:
        print('No')
