n,k = map(int,input().split())
arr = list(map(int,input().split()))

new = [arr[0]] 

for i in range(1,n):
    if new[-1]+arr[i]>=k:
        new.append(arr[i])
    else:
        new.append(k-new[-1])
print(sum(new)-sum(arr))
print(*new,sep=" ")
