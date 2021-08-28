num = input()
numlist = num.split()
sum = 0
for i in numlist:
    sum = sum + int(i)
print("{} + {}  =  {}".format(numlist[0], numlist[1], sum))
print(numlist[0] +" + " +numlist[1] +"  =  " +str(sum) )
