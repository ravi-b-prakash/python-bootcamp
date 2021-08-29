import math
def inputt():
    l = int(input("Enter length: "))
    b = int(input("Enter breadth: "))
    h = int(input("Enter height: "))
    return(l, b, h)
def calculate(l, b, h):   
    k = (l**2) + (b**2) + (h**2)
    v = ((math.pow(b,2)) * (math.pow(h,2)))/ (math.sqrt(k))
    r = math.pow(((0.75*v)/math.pi),(1/3))
    return(v, r)
def output(v, r):
    print("The volume of tromboloid is: %.3f"%(v))
    print("The  radius of the sphere whose volume is same as that of the tromboloid is: %.3f"%(r))
def main():
    l, b, h = inputt()
    v, r = calculate(l, b, h)
    output(v, r)
main()
