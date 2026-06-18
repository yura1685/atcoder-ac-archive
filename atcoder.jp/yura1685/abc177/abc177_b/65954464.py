def dis(x: str, y: str):
    a = 0
    for i in range(len(x)):
        if x[i] != y[i]:
            a += 1
    return a

S = input()
T = input()
ans = 1000

for i in range(len(S)-len(T)+1):
    ans = min(ans, dis(S[i:i+len(T)],T))
print(ans)