a, b, c = map(int,input().split())
s = set([a,b,c])
print('Yes' if len(s) in [1,2] else 'No')