n = int(input())
arr = list(map(int,input().split()))
a = "n"
fives = arr.count(5)
zeros = arr.count(0)

if fives <=9 and zeros==0:
    ans = -1
elif fives <9 and zeros!=0:
    ans = 0
elif fives == 9 and zeros!=0:
    ans = "5"*9 + "0"*zeros
elif fives>9 and zeros!=0:
    a = fives//9
    ans = "5"*(a*9) + "0"*zeros
else:
    ans = -1
print(ans)
