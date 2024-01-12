import math
n,m=map(int,input().split())
steps= 0

l=[]
i=1
while n>m*i*2:
    l.append(m*i)
    i+=1
l.append(m*(i))


if l==[]:
    steps = -1
elif n==m :
    steps = n

elif n<m:
    steps = -1
    

    
else: 
    for x in l:
        for j in range(x,0,-1):
            if j*2 + (x-j) ==n:
                steps = x
                break
            
            if x-j<0:
                steps=-1
                break
        if steps>0:
            break
            


print(steps)