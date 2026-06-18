from more_itertools import run_length

S = input()
T = input()

Sl = list(run_length.encode(S))
Tl = list(run_length.encode(T))

if len(Sl) != len(Tl):
    print('No')
    exit()

else:
    n = len(Sl)
    for i in range(n):
        s, sn = Sl[i]
        t, tn = Tl[i]
        if s != t:
            print('No')
            exit()
        if not (sn == tn or tn >= sn >= 2):
            print('No')
            exit()
print('Yes')