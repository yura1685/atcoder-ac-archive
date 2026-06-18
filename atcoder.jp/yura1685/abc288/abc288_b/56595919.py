n, k = map(int,input().split())
rank_in = []
for i in range(n):
    if i < k:
        rank_in.append(input())
    else:
        a = input()
L = sorted(rank_in)
print('\n'.join(L))