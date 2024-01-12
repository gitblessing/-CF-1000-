n,m= map(int,input().split())
arr = list(map(int,input().split()))
indx = [i  for  i in range(1,n+1)]
ans = arr[0]
while len(indx)!=0:
    if len(arr)==1:
        ans = indx[0]
    if arr[0]<=m:
        indx.pop(0)
        arr.pop(0)
    elif arr[0]>m:
        temp = arr[0]-m
        t2 = indx[0]
        indx.pop(0)
        arr.pop(0)
        arr.append(temp)
        indx.append(t2)
    if len(arr) == 1:
        ans = indx[0] 
print(ans)