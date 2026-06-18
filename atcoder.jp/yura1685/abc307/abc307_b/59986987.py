ssholox = []    
cute = int(input())
for _ in range(cute):
    ssholox.append(list(input()))
for iroha in range(cute):
    for AZKi in range(cute):
        if iroha != AZKi:
            aziro = ssholox[AZKi] + ssholox[iroha]
            teetee = []
            for azukiti in range(len(aziro)):
                teetee.append(aziro[len(aziro)-azukiti-1])
            if aziro == teetee:
                print('Yes')
                exit()
print('No')