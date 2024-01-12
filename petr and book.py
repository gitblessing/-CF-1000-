n = int(input())
arr = list(map(int,input().split()))
i=0
while n>=0:
    n-=arr[i]
    i+=1
    if n<=0:
        ans = i
        break
    if i==7:
        i=0

print(ans)