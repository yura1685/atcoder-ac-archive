from sortedcontainers import SortedList

N = int(input())
S = input()
a = [i for i in range(N) if S[i] == 'A']
b = [i for i in range(N) if S[i] == 'B']
a.reverse(); b.reverse()
SL = SortedList(range(N+1))

for k in range(N):
    if k % 2:
        if a:
            i = a.pop()
            SL.discard(i)
    else:
        if b:
            i = b.pop()
            SL.discard(i)
    if S[SL[0]] == 'A':
        print('Alice')
    else:
        print('Bob')