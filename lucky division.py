lis = [4,7,44,77,47,74,444,447,474,477,744,777,774,747]
n = int(input())
last = len(lis)-1

yes = 0
for i in lis:
    if n%i==0:
        yes+=1
    else:
        yes+=0
if yes>0:
    print("YES")
else:
    print("NO")