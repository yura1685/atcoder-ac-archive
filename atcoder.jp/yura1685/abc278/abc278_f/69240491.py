from functools import cache

N = int(input())
S = tuple(input() for _ in range(N))
X = [s[0] for s in S]

@cache
def dfs(s, h, p): # 現在の単語の集合s, 先頭の文字h, プレイヤーp
    flag = True
    W = []
    for i in range(len(s)):
        words = s[i]
        if words[0] == h:
            flag = False
            W.append(dfs(tuple(s[j] for j in range(len(s)) if i != j), words[-1], p^1))
    # この盤面から始めたときの勝者を返す
    if flag:
        return p^1
    else:
        return p if p in W else p^1

print('First' if 0 in [dfs(S, x, 0) for x in X] else 'Second')