from more_itertools import batched

W = int(input())
S = 'DiscoPresentsDiscoveryChannelProgrammingContest2016'

L= list(batched(S, n=W))
for i in L:
    print(''.join(i))