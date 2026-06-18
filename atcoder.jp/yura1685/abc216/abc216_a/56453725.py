N = input()
Y = int(N[-1])
X = N[:-2]
if Y == 0 or Y == 1 or Y == 2:
    print(X+'-')
elif Y == 3 or Y == 4 or Y == 5 or Y == 6:
    print(X)
else:
    print(X+'+')