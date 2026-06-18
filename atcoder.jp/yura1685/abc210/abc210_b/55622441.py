N = int(input())
S = input()
i = 0
while S[i] == '0':
    i += 1
print('Takahashi' if i % 2 == 0 else 'Aoki')