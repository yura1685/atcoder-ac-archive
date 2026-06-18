O = input()
E = input()
password = O[0]
for i in range(len(O)+len(E)-1):
    if i % 2 == 0:
        password += E[i//2]
    else:
        password += O[i//2+1]
print(password)