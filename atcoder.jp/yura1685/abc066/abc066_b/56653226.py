S = input()
while True:
    S = S[:-2]
    l = len(S)
    if S[:l//2] == S[l//2:]:
        print(l);exit()