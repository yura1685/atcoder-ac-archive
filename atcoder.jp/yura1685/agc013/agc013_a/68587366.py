N = int(input())
A = list(map(int,input().split()))

i = 0
X = []
ans = 0
while i < N:
    if not X:
        ans += 1
        X.append(A[i])
        d = '-'
        i += 1
    else:
        if d == '-':
            if X[-1] > A[i]:
                d = 'v'
            elif X[-1] < A[i]:
                d = '^'
            X.append(A[i])
            i += 1
        elif d == '^':
            if X[-1] <= A[i]:
                X.append(A[i])
                i += 1
            else:
                X.clear()
        else:
            if X[-1] >= A[i]:
                X.append(A[i])
                i += 1
            else:
                X.clear()

print(ans)