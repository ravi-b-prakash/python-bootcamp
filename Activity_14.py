def prime(num):
    f=0
    for i in range(1, num):
        if(num%i==0):
            f+=1
    if(f==1):
        print("%d is prime"%(num))
    else:
        print("%d is composite"%(num))
def main():
    num = int(input("enter a number: "))
    prime(num)
main()

