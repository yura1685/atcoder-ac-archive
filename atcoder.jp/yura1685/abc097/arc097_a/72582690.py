S = input()
N = len(S)
K = int(input())
s = set()
for i in range(1,6):
    for j in range(N-i+1):
        s.add(S[j:j+i])
print(sorted(s)[K-1])