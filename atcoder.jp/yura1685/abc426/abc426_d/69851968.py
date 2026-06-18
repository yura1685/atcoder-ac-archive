from more_itertools import run_length

T = int(input())
for _ in range(T):
    N = int(input())
    S = input()
    rl = list(run_length.encode(S))
    len0, len1 = 0, 0
    for num, cnt in rl:
        if num == '0':
            len0 = max(len0, cnt)
        else:
            len1 = max(len1, cnt)
    cnt0, cnt1 = S.count('0'), S.count('1')
    score0, score1 = 2*cnt0 + cnt1 - 2*len0, 2*cnt1 + cnt0 - 2*len1
    print(min(score0, score1))