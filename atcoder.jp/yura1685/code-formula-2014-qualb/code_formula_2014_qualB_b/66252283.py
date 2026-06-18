N = list(input())
S1=N[-2::-2];S2=N[::-2]
S1=map(int,S1);S2=map(int,S2)
print(sum(S1),sum(S2))