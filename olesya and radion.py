n,m = map(int,input().split())
small,large = 10**(n-1),10**n

for i in range(small+1,large):
    if i%m==0:
        ans = i
        break
else:
    ans=-1
print(ans)