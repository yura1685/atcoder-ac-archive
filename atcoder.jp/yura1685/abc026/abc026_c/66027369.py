N = int(input())
buka = {}

for i in range(2,N+1):
    B = int(input())
    if buka.get(B) == None:
        buka[B] = [i]
    else:
        buka[B].append(i)

def money(n):
    if buka.get(n) == None:
        return 1
    c = []
    for man in buka[n]:
        c.append(money(man))
    return max(c) + min(c) + 1

print(money(1))