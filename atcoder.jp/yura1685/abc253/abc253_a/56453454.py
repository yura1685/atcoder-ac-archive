a,b,c=map(int,input().split())
print('Yes' if b == a + b + c - max(a,b,c) - min(a,b,c) else 'No')