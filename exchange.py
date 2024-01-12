import math
for no_testcase in range(int(input())):
    n,a,b = map(int,input().split())
    games = 0
    
    if a>b:
        games = 1
    elif a==b:
        games = math.ceil(n/a)
    elif a<b:
        games = math.ceil(n/a)
    print(int(games))