n,m = map(int,input().split())
arr = list(map(int,input().split()))
curr = 1 
time = 0
for i in arr:
    if i > curr:
        time+=i-curr
        curr = i
    elif i<curr:
        time+= n-curr+i
        curr = i
    else:
        pass
print(time)