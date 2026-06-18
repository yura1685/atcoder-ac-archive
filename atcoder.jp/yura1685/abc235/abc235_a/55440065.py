abc = int(input())
a = abc // 100
b = (abc - 100 * a) // 10
c = (abc - 100 * a - 10 * b)
print(111*(a+b+c))