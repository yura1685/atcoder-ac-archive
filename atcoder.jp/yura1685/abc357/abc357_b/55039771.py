S = input()
a = 0
for i in range(len(S)):
    if S[i].isupper():
        a += 1
if a > len(S)//2:
    print(S.upper())
else:
    print(S.lower())