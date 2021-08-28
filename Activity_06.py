num = input()
numlist = num.split()
sliced_numlist = numlist[0:3]
for i in range(5):
    numlist[i] = int(numlist[i])
for i in range(3):
    sliced_numlist[i] = int(sliced_numlist[i])
numlist[0] = 0
numlist[4] = 0
print("sliced list = ",end = " ")
print(sliced_numlist)
sliced_numlist[0] = 0
sliced_numlist[2] = 0
print("replaced list-1 = ",end = " ")
print(numlist)
print("replaced list-2 = " ,end =" ")
print(sliced_numlist)
