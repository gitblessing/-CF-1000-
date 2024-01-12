# one test case is failed but dont know why 

for no_testcase in range(int(input())):
    x,y = map(int,input().split())
    a,b = map(int,input().split())
    money = 0
    
    if x==y:
        money = min( a*(abs(x)) , b*(abs(x)))
    
    elif x<0 and y<0:
        diff_x = abs(x)
        diff_y = abs(y)
        money = min((abs(x-y)*b) + (min(x,y) - abs(x-y))*a , a*(diff_x+diff_y))
    elif x<0 and y>0:
        diff_x = abs(x)
        diff_y = abs(y-0)
        money = (a*diff_x) + (a*diff_y)
    elif x>0 and y<0:
        diff_x,diff_y = abs(x),abs(y)
        money = (a*(diff_x + diff_y))
    elif x>0 and y>0:
        diff_x,diff_y = abs(x),abs(y)
        money = min((abs(x-y)*a)+(max(x,y) - abs(x-y))*b , a*(diff_x+diff_y))
    elif x==0 and y>0:
        money = abs(y)*a
    elif x==0 and y<0:
        money = abs(y)*a
    elif y==0 and x>0:
        money = abs(x)*a
    elif y==0 and x<0:
        money = abs(x)*a
    
    print(money)