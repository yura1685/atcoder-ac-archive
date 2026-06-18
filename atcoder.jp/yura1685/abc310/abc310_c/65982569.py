def reverse(s:str):
    t = list(s)
    t.reverse()
    s2 = ''.join(t)
    return min(s, s2)

N = int(input())

dango = set()
for _ in range(N):
    s = input()
    S = reverse(s)
    dango.add(S)

print(len(dango))