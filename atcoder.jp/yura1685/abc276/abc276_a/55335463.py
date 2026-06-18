S = input()
if 'a' not in S:
    print(-1)
    exit()
for i in range(len(S)):
    if S[len(S)-1-i] == 'a':
        print(len(S)-i)
        exit()