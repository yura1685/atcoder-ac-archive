N = int(input())
S = input()
T = input()

dif = 0
for i in range(N):
    if S[i] != T[i]:
        dif +=1

print(dif)