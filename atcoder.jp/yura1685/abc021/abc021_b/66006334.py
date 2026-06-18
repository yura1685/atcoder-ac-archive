n = int(input())
a, b = map(int,input().split())
k = int(input())
p = list(map(int,input().split()))
p = [a] + p + [b]
print('YES' if len(set(p)) == k+2 else 'NO')