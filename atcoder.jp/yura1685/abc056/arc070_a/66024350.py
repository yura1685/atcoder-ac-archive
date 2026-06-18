X = int(input())
D = int(((1+8*X)**(0.5) - 1)/2) - 1

for i in range(D,D+100):
    if i*(i+1) >= 2*X:
        print(i)
        exit()