S = input()
T = input()
n = len(T)

l = [False] * (n+1)
r = [False] * (n+1)
l[0], r[0] = True, True
def f(a,b):
    if a == b or a == '?' or b == '?':
        return True
    else:
        return False

flag1, flag2 = True, True
for i in range(n):
    if f(S[i], T[i]) and flag1:
        l[i+1] = True
    else:
        flag1 = False
    if f(S[-i-1], T[-i-1]) and flag2:
        r[i+1] = True
    else:
        flag2 = False

for i in range(n+1):
    if l[i] and r[-i-1]:
        print('Yes')
    else:
        print('No')