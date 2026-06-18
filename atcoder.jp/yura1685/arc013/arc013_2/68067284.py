C = int(input())
l = [max(i) for i in list(zip(*[sorted(map(int,input().split())) for _ in range(C)]))]
print(l[0]*l[1]*l[2])