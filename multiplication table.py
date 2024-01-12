import math
n,m = map(int,input().split())
coun = 0
if m==1 or n==m==1:
    coun=1
elif m>n**2:
    coun = 0
else:
    for i in range(2,math.floor(m/2)+1):
        if m%i==0 and m/i <=n:
            coun+=1
    
if m<=n and n!=1 and m!=1:
    coun+=2

print(coun)
        
    