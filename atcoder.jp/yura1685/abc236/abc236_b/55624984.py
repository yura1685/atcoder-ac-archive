N = int(input())
A = list(map(int,input().split()))
card = [0]*N
for i in range(4*N-1):
    card[A[i]-1] += 1
print(card.index(3)+1)