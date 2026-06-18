s = input()
k = int(input())

pas = set()
for i in range(len(s)-k+1):
    p = s[i:i+k]
    pas.add(p)

print(len(pas))