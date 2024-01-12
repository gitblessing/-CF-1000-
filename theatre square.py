import math
n,m,a =map(int,input().split())
b,c =n,m
count_c,count_b = 0,0

if a ==1:
    print(n*m)

else:
        

    while b>0:
        b-=a
        count_b+=1
        
    while c>0:
        c-=a
        count_c+=1

    print(count_b*count_c)


        
    