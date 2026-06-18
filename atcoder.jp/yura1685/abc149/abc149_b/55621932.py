Taka, Aoki, K = map(int,input().split())
if Taka + Aoki < K:
    Taka, Aoki = 0, 0
elif Taka < K:
    Taka, Aoki = 0, Aoki - (K - Taka)
else:
    Taka, Aoki = Taka - K, Aoki
print(Taka, Aoki)