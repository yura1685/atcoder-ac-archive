N = int(input())

S = 'a'

ans = []
def f(x):
    if len(x) == N:
        ans.append(x)
        return 
    for alp in 'abcdefghij'[:ord(max(x))-ord('_')]:
        f(x+alp)

f(S)

for yura in ans:
    print(yura)