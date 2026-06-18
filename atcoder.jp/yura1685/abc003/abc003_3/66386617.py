N, K = map(int,input().split())
R = list(map(int,input().split()))
R.sort(reverse=True)

rating = 0

for i in range(K):
    rating = (rating+R[K-i-1])/2

print(rating)