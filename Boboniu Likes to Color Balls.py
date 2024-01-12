
for no_testcase in range(int(input())):
    r,g,b,w = map(int,input().split())

    if r%2!=0 and g%2!=0 and b%2!=0 and w%2!=0 and min(r,g,b,w)>=1:
        print("Yes")
    elif r%2!=0 and g%2!=0 and b%2!=0 and w%2==0 and min(r,g,b,w)>=1:
        print("Yes")
    elif r%2!=0 and g%2!=0 and b%2==0 and w%2==0:
        print("No")
    elif r%2!=0 and g%2!=0 and b%2==0 and w%2!=0 and min(r,g,b,w)>=1:
        print("Yes")
    elif r%2!=0 and g%2==0 and b%2!=0 and w%2==0:
        print("No")
    elif r%2!=0 and g%2==0 and b%2!=0 and w%2!=0 and min(r,g,b,w)>=1:
        print("Yes") 
    elif r%2!=0 and g%2==0 and b%2==0 and w%2==0:
        print("Yes")
    elif r%2!=0 and g%2==0 and b%2==0 and w%2!=0:
        print("No")
    elif r%2==0 and g%2!=0 and b%2!=0 and w%2==0:
        print("No")
    elif r%2==0 and g%2!=0 and b%2!=0 and w%2!=0 and min(r,g,b,w)>=1:
        print("Yes")
    elif r%2==0 and g%2!=0 and b%2==0 and w%2==0:
        print("Yes")
    elif r%2==0 and g%2!=0 and b%2==0 and w%2!=0:
        print("No")
    elif r%2==0 and g%2==0 and b%2!=0 and w%2==0:
        print("Yes")
    elif r%2==0 and g%2==0 and b%2!=0 and w%2!=0:
        print("No")
    elif r%2==0 and g%2==0 and b%2==0 and w%2==0:
        print("Yes")
    elif r%2==0 and g%2==0 and b%2==0 and w%2!=0:
        print("Yes")
    else:
        print("No")
   