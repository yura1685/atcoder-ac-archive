S = input()
a = 1
if S[0] == '<' and S[len(S)-1] == '>':
    a = 0
    for i in range(1,len(S)-1):
        if S[i] != '=':
            a = 1
if a == 0:
    print('Yes')
else:
    print('No')