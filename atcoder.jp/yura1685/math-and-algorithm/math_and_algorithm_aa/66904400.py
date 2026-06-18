# 本を持っていないので普通にソート関数を使います。ごめん
# いつかちゃんとソートアルゴリズムを勉強します

N = int(input())
A = list(map(int,input().split()))
A.sort()
print(*A)