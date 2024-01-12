n,m = map(int,input().split())
l=[]
for i in range(m):
    a,b = map(str,input().split())
    l.append(a)
    l.append(b)
word = list(map(str,input().split()))
out = []
for i in word:
    t = l.index(i)
    if t%2==0:
        if len(l[t])>len(l[t+1]):
            out.append(l[t+1])
        else:
            out.append(l[t])
    else:
        if len(l[t])>len(l[t-1]):
            out.append(l[t-1])
        else:
            out.append(l[t])
    
print(*out,sep=" ")