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
        isprime = False
    else:
        isprime = True
    return(isprime)
def output(isprime, num):
    if(isprime==True):
        print("%d is prime"%(num))
    else:
        print("%d is composite"%(num))
def main():
    num = inputt()
    isprime = prime(num)
    output(isprime, num)
main()
