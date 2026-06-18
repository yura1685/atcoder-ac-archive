M=int(input());X=[-1]*M
for y in range(M):X[y**3%M]=y
for x in X:print(x)