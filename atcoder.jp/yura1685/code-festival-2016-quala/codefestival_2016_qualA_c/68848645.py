S = input()
K = int(input())
X = [ord(s)-97 for s in S]

for i in range(len(X)):
    if X[i] and X[i] + K > 25:
        K -= (26-X[i])
        X[i] = 0
    if K == 0:
        break

X[-1] = (X[-1] + K) % 26

ans = [chr(x+97) for x in X]
print(''.join(ans))