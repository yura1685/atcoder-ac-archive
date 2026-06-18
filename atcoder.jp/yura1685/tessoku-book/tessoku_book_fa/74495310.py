D = int(input())
kabuka = [int(input())]
for _ in range(D-1):
    A = int(input())
    kabuka.append(kabuka[-1] + A)
Q = int(input())
for _ in range(Q):
    S, T = map(int, input().split())
    print(S if kabuka[S-1] > kabuka[T-1] else T if kabuka[S-1] < kabuka[T-1] else 'Same')