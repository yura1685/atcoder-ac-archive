from collections import defaultdict

S = input()
T = input()

alpS = defaultdict(int)
for s in S:
    alpS[s] += 1

alpT = defaultdict(int)
for t in T:
    alpT[t] += 1

for alp in set('qwertyuiopasdfghjklzxcvbnm') - set('atcoder'):
    if alpS[alp] != alpT[alp]:
        print('No')
        exit()

atS = alpS['@']
atT = alpT['@']

for alp in 'atcoder':
    if alpS[alp] < alpT[alp]:
        atS -= alpT[alp] - alpS[alp]
    elif alpS[alp] > alpT[alp]:
        atT -= alpS[alp] - alpT[alp]

if atS == atT >= 0:
    print('Yes')

else:
    print('No')