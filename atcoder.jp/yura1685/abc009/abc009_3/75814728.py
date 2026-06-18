from collections import Counter

N, K = map(int, input().split())
S = input()

cnt_S = Counter(S)
nokori = Counter(S)

T = []
diff = 0

alp = 'abcdefghijklmnopqrstuvwxyz'

for i in range(N):
    cnt_S[S[i]] -= 1
    for c in alp:
        if nokori[c] > 0:
            nokori[c] -= 1
            
            next_diff = diff
            if c != S[i]:
                next_diff += 1
            M = 0
            for ch in alp:
                M += min(nokori[ch], cnt_S[ch])           
            
            if next_diff + N - 1 - i - M <= K:
                T.append(c)
                diff = next_diff
                break
            
            nokori[c] += 1

print("".join(T))