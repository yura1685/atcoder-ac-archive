S = input()
a, b = map(int, input().split())

q = S[:a-1]
w = S[b-1]
e = S[a:b-1]
r = S[a-1]
t = S[b:]
print(q+w+e+r+t)