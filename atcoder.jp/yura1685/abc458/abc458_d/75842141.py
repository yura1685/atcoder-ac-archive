from sortedcontainers import SortedList

S = SortedList()
X = int(input())
S.add(X)
Q = int(input())
for i in range(Q):
    A, B = map(int, input().split())
    S.add(A)
    S.add(B)
    print(S[i+1])