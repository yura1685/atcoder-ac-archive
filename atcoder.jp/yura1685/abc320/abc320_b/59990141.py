def kai(x): #str入力
    for i in range(len(x)):
        if x[i] != x[len(x)-i-1]:
            return 0
    return len(x)

l = 1
S = input()
for i in range(len(S)-1):
    for j in range(i+1,len(S)):
        if S[i] == S[j]:
            l = max(l,kai(S[i:j+1]))
print(l)