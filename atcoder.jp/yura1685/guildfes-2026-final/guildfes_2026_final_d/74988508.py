N = int(input())
S = [input() for _ in range(N)]
S.sort(key=lambda x: len(x), reverse=True)
print(''.join(s[0].upper() for s in S))