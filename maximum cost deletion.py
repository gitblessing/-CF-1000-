for no_testcase in range(int(input())):
    n,a,b = map(int,input().split())
    s = str(input())
    points = 0
    if a<0 and b>0:
        points += a*n + b*n
    l= list(s)
    
 