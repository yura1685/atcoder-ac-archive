S = input()
L = []
for i in range(len(S)):
    if S[len(S)-i-1] == '0':
        L.append('0')
    elif S[len(S)-i-1] == '1':
        L.append('1')
    elif S[len(S)-i-1] == '6':
        L.append('9')
    elif S[len(S)-i-1] == '8':
        L.append('8')
    elif S[len(S)-i-1] == '9':
        L.append('6')
a = ''.join(L)
print(a)