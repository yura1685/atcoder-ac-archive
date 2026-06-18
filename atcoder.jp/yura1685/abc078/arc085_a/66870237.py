N, M = map(int,input().split())

sub = 1900*M + 100*(N-M)
print(sub*2**M)