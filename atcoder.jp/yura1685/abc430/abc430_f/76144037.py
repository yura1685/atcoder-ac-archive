def solve():
    N = int(input())
    S = 'X' + input() + 'X'
    rightR = [0] * N
    rightL = [0] * N
    leftR = [0] * N
    leftL = [0] * N
    for i in range(N):
        if S[i] == 'L':
            leftL[i] = 1
            leftR[i] = -1
        elif S[i] == 'R':
            leftR[i] = 1
            leftL[i] = -1
        if S[i+1] == 'L':
            rightL[i] = 1
            rightR[i] = -1
        elif S[i+1] == 'R':
            rightR[i] = 1
            rightL[i] = -1
    for i in range(1, N):
        if leftL[i] < 0:
            leftL[i] = 0
        else:
            leftL[i] += leftL[i-1]
        if leftR[i] < 0:
            leftR[i] = 0
        else:
            leftR[i] += leftR[i-1]
    for i in range(N-2, -1, -1):
        if rightR[i] < 0:
            rightR[i] = 0
        else:
            rightR[i] += rightR[i+1]
        if rightL[i] < 0:
            rightL[i] = 0
        else:
            rightL[i] += rightL[i+1]
    C = [0] * N
    for i in range(N):
        R = rightR[i] + leftL[i]
        L = rightL[i] + leftR[i]
        if L > 0:
            C[0] -= 1
            C[L] += 1
        if R > 0:
            C[N-R] -= 1
    for i in range(N-1):
        C[i+1] += C[i]
    for i in range(N):
        C[i] += N
    print(*C)

for _ in range(int(input())):
    solve()