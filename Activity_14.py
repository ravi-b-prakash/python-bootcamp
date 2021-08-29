import math
def inputt():
    num = int(input("enter a number: "))
    return num
def prime(num):
    f=0
    for i in range(2, int(math.sqrt(num))+1):
        if(num%i==0):
            f=1
            break
    if(f==1):
        print("%d is composite"%(num))
    else:
        print("%d is prime"%(num))
def main():
    num = inputt()
    prime(num)
main()
