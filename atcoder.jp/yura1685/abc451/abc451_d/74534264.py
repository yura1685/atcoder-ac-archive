L = [str(1 << i) for i in range(30)]
good = set()

def f(S):
    good.add(S)
    LS = len(S)
    for s in L:
        ls = len(s)
        if LS + ls < 9:
            f(S+s)
        elif LS + ls == 9:
            good.add(S+s)

f('')
ans = sorted(int(n) for n in good if n)

print(ans[int(input())-1])