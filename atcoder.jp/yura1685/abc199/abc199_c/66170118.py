N = int(input())

S = list(input())
Q = int(input())
non_flip = 1

for _ in range(Q):
    T, A, B = map(int,input().split())
    if T == 2:
        non_flip = 1 - non_flip
    else:
        if non_flip:
            S[A-1], S[B-1] = S[B-1], S[A-1]
        else:
            if   A <= N: A += N
            elif A >  N: A -= N
            if   B <= N: B += N
            elif B >  N: B -= N
            S[A-1], S[B-1] = S[B-1], S[A-1]

if non_flip:
    print(''.join(S))
else:
    print(''.join(S[N:]) + ''.join(S[:N]))