n = int(input())
t = n%4
if n==0: 
    ans = 1
elif t==0:
    ans = 6
elif t==1:
    ans = 8
elif t==2:
    ans = 4
elif t==3:
    ans = 2


print(ans)