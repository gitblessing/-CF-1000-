n,m = map(int,input().split())
x = m/n

move=0
while x>1:
    if x%2==0:
        x = x/2
        move+=1
        continue 
    elif x%3==0:
        x = x/3
        move+=1
        continue
    else:
        move = -1
        break
if n==m:
    print(0)
elif x!=1:
    print(move)
else:
    print(move)