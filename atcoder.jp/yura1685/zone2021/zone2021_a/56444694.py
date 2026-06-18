S = input()
ans = 0
for i in range(len(S)-3):
    if S[i] == 'Z' and S[i+1] == 'O' and S[i+2] == 'N' and S[i+3] == 'e':
        ans += 1
print(ans)