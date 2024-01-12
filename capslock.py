x = input()
t= sorted(x)
if len(x)==1 and x.islower():
    print(x.upper())
    
elif x.isupper():
    print(x.lower())
elif (x[0]).islower() and (x[1:].isupper()):
    print(x[0].upper() + (x[1:]).lower())
    
elif (x[0]).isupper() and (x[1:]).islower():
    print(x)
elif (x[0]).islower() and t[1].isupper():
    print(x)
else:
    print(x)