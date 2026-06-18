S = input()
print('Yes' if all([s.isdigit() if i != 3 else s == '-' for i, s in enumerate(S)]) else 'No')