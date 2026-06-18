N = int(input())
man_to_girl = [0] + list(map(int,input().split()))
man_to_num = [0] + list(map(int,input().split()))
num_to_man = [0]*(N+1)


for i in range(1,N+1):
    num_to_man[man_to_num[i]] = i

for num in range(1,N+1):
    man = num_to_man[num]
    girl = man_to_girl[man]
    ans = man_to_num[girl]
    print(ans,end=' ')