lis=[]
for no_testcase in range(int(input())):
    n = str(input())
    lis.append(n)


frequency = {}

# iterating over the list
for item in lis:
   # checking the element in dictionary
   if item in frequency:
      # incrementing the counr
      frequency[item] += 1
   else:
      # initializing the count
      frequency[item] = 1

Keymax = max(zip(frequency.values(), frequency.keys()))[1]
print(Keymax)