import math
l = int(input("Enter length: "))
b = int(input("Enter breadth: "))
h = int(input("Enter height: "))
k = (l**2) + (b**2) + (h**2)
v = ((math.pow(b,2)) * (math.pow(h,2)))/ (math.sqrt(k))
print("The volume of tromboloid is: %.3f"%(v))
r = math.pow(((0.75*v)/math.pi),(1/3))
print("The  radius of the sphere whose volume is same as that of the tromboloid is: %.3f"%(r))
