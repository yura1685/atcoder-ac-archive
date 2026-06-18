yabai, kigen, eat = map(int,input().split())
if eat <= kigen:
    print('delicious')
elif eat <= kigen + yabai:
    print('safe')
else:
    print('dangerous')