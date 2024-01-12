import math
for no_testcase in range(int(input())):
    a,b,n,s = map(int,input().split())
    t = s//n
    if t<=a and s-(n*t)<=b:
        print("YES")
    elif s-(n*a)<=b and t>a:
        print("YES")
    else:
        print("NO")