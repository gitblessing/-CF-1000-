import math 
a,b= map(int,input().split())

candle=a
extra = 10
while a>=b:
    extra  = math.floor(a/b)
    a = a-b*extra +(extra)
    candle+=extra

    
    
print(candle)