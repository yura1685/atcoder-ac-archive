N, A, B = map(int,input().split())
S = input()

passed = 0
kaigai = 0

for x in S:
    if x == 'a':
        if passed < A+B:
            print('Yes')
            passed += 1
        else:
            print('No')
    if x == 'b':
        if passed < A+B and kaigai < B:
            print('Yes')
            passed += 1
            kaigai += 1
        else:
            print('No')
    if x == 'c':
        print('No')