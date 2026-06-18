from sortedcontainers import SortedList

N, Q = map(int, input().split())
M = 2 * 10 ** 5
Kinder = [SortedList() for _ in range(M + 1)]
Rating = [0] * (N+1)
Where = [0] * (N+1)
for i in range(1,N+1):
    A, B = map(int, input().split())
    Kinder[B].add(A)
    Where[i] = B
    Rating[i] = A

Score = SortedList()
for K in Kinder:
    if K:
        Score.add(K[-1])

for _ in range(Q):
    C, D = map(int, input().split())
    A, B = Rating[C], Where[C]
    Where[C] = D
    if Kinder[B][-1] > A:
        Kinder[B].discard(A)
    else:
        Kinder[B].discard(A)
        Score.discard(A)
        if Kinder[B]:
            Score.add(Kinder[B][-1])
    if Kinder[D] and Kinder[D][-1] > A:
        Kinder[D].add(A)
    else:
        if not Kinder[D]:
            Kinder[D].add(A)
            Score.add(A)
        else:
            Score.discard(Kinder[D][-1])
            Kinder[D].add(A)
            Score.add(A)
    print(Score[0])