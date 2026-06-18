N = int(input())
sum_rate = 0
member = []
for i in range(N):
    name, rate = map(str,input().split())
    sum_rate += int(rate)
    member.append(name)
winner_num = sum_rate % N
dictionary = sorted(member)
print(dictionary[winner_num])