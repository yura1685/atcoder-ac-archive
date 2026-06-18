def check(s):
    if s.count('i')==1 and s.count('n')==2 and s.count('d')==2 and s.count('e') == 2 and s.count('o')==1 and s.count('w')==1:
        if len(s) == 9:
            return True
    return False

n = int(input())
for _ in range(n):
    s = input()
    if check(s):
        print('YES')
    else:
        print('NO')