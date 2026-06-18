S = input()
ans = 10000
for i in range(len(S)-2):
    x = int(S[i:i+3])
    ans = min(ans,abs(x-753))

print(ans)