N, K = map(int,input().split())
S = input().count('1')
print('No' if (K-S)%2 else 'Yes')