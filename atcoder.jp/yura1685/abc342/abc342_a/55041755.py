S = input()
N = len(S)
for i in range(N):
    if S.count(S[i]) == 1:
      print(i + 1)