import math
for no_testcase in range(int(input())):
    n = int(input())
    mini = n
    ans = []
    
    if n%2==0:
        x = int(n/2)
    elif n%2!=0:
        x = int((n-1)/2)
        
    for i in range(1,x+1):
        if math.lcm(i,n-i)<=mini:
            mini = math.lcm(i,n-i)
            ans = [i,n-i]
    
    print(*ans,sep=" ")