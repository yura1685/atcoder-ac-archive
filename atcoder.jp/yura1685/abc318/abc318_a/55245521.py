N, M, P =map(int, input().split())
moonday = 0
if M > N:
    print(moonday)
    exit()
moonday += 1
N = N - M
moonday += N // P
print(moonday)