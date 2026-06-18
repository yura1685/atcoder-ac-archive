eq0 = [2,2,2,3,3,6]
eq1 = [1]
eq2 = [2,2,3,3,3,3,6,6]

for i in range(40000):
    for _ in range(4):
        eq0.append(2*eq0[i])
        eq1.append(2*eq1[i])
        eq2.append(2*eq2[i])

def solve():
    N = int(input())
    if N in [2,3,5]:
        print('No')
        return
    print('Yes')
    if N % 3 == 0:
        l = (N-6) // 3
        r = l + N
        print(*eq0[l:r])
    elif N % 3 == 1:
        l = (N-1) // 3
        r = l + N
        print(*eq1[l:r])
    else:
        l = (N-8) // 3
        r = l + N
        print(*eq2[l:r])

T = int(input())
for _ in range(T):
    solve()