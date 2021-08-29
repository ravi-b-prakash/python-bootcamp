import math
def prime(num):
    f=0
    for i in range(2, int(math.sqrt(num))+1):
        if(num%i==0):
            f+=1
    if(f==0):
        print("%d is prime"%(num))
    else:
        print("%d is composite"%(num))
def main():
    num = int(input("enter a number: "))
    prime(num)
main()
