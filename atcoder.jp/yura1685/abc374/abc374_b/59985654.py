S = input()
T = input()
if S == T:
    print(0)
else:
    if len(T) > len(S):
        S, T = T, S
    n = len(T)
    for i in range(n):
        if S[i] != T[i]:
            print(i+1)
            exit()
    print(n+1)