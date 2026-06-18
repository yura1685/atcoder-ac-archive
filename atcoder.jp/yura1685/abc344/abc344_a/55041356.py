S = input()
for i in range(len(S)):
    if S[i] == '|':
        tate1 = i
        break
for i in range(len(S)):
    if S[len(S)-i-1] == '|':
        tate2 = len(S)-i
        break
print(S[:tate1]+S[tate2:])