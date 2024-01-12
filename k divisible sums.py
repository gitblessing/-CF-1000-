for no_testcase in range(int(input())):
    n,k = map(int,input().split())
    if k>n:
        if k%n==0:
            ans = (k//n)
        else:
            ans = (k//n) + 1
    elif k==n:
        ans = 1
    else:
        if (n/k).is_integer():
            ans = 1
        else:
            ans = 2
    print(ans)        
            