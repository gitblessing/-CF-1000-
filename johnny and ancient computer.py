# CODE IS WRONG

def move_check(b=1,a=1):
    moves = 0
    power = math.log2(b/a)
    if power>=3:
        moves += math.ceil(power/3)
    elif power<=2:
        moves +=1
    return moves

import math
for no_testcase in range(int(input())):
    a,b = map(int,input().split())
    moves = 0
    if b==a:
        moves = 0
    elif b>a:
        if a==1:
            if math.log2(b).is_integer() == True:
               moves = move_check(b)
            else:
               moves = -1
        elif math.log2(b/a).is_integer() == True:
            moves = move_check(b,a)
            
        else:
            moves=-1
        
            
            
    elif b<a:
        if b==1:
            if math.log2(a).is_integer() == True:
               moves = move_check(a)
            else:
               moves = -1
        elif math.log2(a/b).is_integer() == True:
            moves = move_check(a,b)
            
        else:
            moves=-1
    
    print(moves)