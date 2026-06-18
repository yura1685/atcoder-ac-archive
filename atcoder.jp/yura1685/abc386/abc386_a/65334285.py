A,B,C,D = map(int,input().split())
print('Yes' if len(set([A,B,C,D])) == 2 else 'No')