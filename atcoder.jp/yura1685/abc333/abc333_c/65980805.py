N = int(input())

rep = [(10**i-1)//9 for i in range(1,13)]
repreprep = set()

for i in rep:
    for j in rep:
        for k in rep:
            repreprep.add(i+j+k)
repreprep = list(repreprep)
repreprep.sort()
print(repreprep[N-1])