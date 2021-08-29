import math
def inputt():
    num = int(input("enter a number: "))
    return num
def prime(num):
    isprime = True
    for i in range(2, int(math.sqrt(num))+1):
        if(num%i==0):
            isprime = False
            break
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
