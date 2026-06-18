N = int(input())
A = list(map(int,input().split()))
ride, ride_min = 0, 0
for i in A:
    ride += i
    ride_min = min(ride_min,ride)
print(ride-ride_min)