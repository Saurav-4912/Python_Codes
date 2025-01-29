tup = (12,56,34,65,23)

maxNum = tup[0]
for i in range(1,len(tup)):
 if tup[i] > maxNum:
  maxNum = tup[i]

print("Maximum Number : " , maxNum)
