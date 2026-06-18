from more_itertools import run_length

S = input()
l = list(run_length.encode(S))
print(len(l)-1)