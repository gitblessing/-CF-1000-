def vol(rad):
    return 4*(3.14)*rad*rad

def range_check(num,mini,maxi):
    if num in range(mini,maxi+1):
        return True
    
    else:
        return False
    
def palindrome_check(string):
    for x in range(len(string)):
        if string[x]==string[-(x+1)]:
            continue
        else:
            return False
    return True

