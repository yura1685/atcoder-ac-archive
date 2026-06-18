iroha = []
for kawaii in range(10):
    azki = input()
    if azki != '..........':
        iroha.append(kawaii+1)
        gozaru = azki
print(iroha[0],iroha[-1])
kazama = iroha[0]
azkiti = []
for aziro in range(10):
    if gozaru[aziro] == '#':
        azkiti.append(aziro+1)
print(azkiti[0],azkiti[-1])