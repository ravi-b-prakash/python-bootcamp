num = input()
numlist = num.split()
sum = 0
for i in numlist:
    sum += int(i)
print("Sum of all the numbers is = "+str( sum))
