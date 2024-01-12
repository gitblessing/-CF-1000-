from itertools import groupby
n = int(input())
arr = list(input())
ans = 0
z = [len(list(group)) for key, group in groupby(sorted(arr))]

for j in z:
    if j%n!=0:
        ans = -1
        break
    else:
        pass

if ans == 0:
    print()