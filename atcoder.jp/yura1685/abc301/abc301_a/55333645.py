N = int(input())
S = input()
ta = S.count('T')
if ta > N - ta:
    print('T')
elif ta < N - ta:
    print('A')
else:
    S = S[:-1]
    ta = S.count('T')
    if ta > N - 1 - ta:
        print('T')
    else:
        print('A')