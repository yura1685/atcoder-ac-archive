A = input()
N = len(A)
same, diff = 0, 0
for i in range(N//2):
    if A[i] == A[N-i-1]:
        same += 1
    else:
        diff += 1
odd = N % 2

if diff == 0: print(same*50)

elif diff == 1: print(same*50 + diff*48 + 25*odd)

else: print(same*50 + diff*50 + 25*odd)