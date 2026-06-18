N = int(input())
s = set()
for _ in range(N):
    A, B = map(int,input().split())
    s.add((min(A,B),max(A,B)))
print(len(s))