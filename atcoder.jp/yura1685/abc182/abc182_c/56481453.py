N = input()
mod3_0 = 0
mod3_1 = 0
mod3_2 = 0
for i in range(len(N)):
    if int(N[i]) % 3 == 0:
        mod3_0 += 1
    elif int(N[i]) % 3 == 1:
        mod3_1 += 1
    else:
        mod3_2 += 1

if (mod3_2 * 2 + mod3_1) % 3 == 0:
    print(0)
elif (mod3_2 * 2 + mod3_1) % 3 == 1:
    if mod3_1 >= 1:
        if mod3_1 == len(N):
            print(-1)
        else:
            print(1)
    elif mod3_2 >= 2:
        if mod3_2 == len(N):
            print(-1)
        else:
            print(2)
    else:
        print(-1)
else:
    if mod3_2 >= 1:
        if mod3_2 == len(N):
            print(-1)
        else:
            print(1)
    elif mod3_1 >= 2:
        if mod3_1 == len(N):
            print(-1)
        else:
            print(2)
    else:
        print(-1)