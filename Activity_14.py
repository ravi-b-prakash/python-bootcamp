def prime(num):
    f=0
    for i in range(1, num+1):
        if(num%i==0):
            f+=1
    if(f==2):
        print("%d is prime"%(num))
    else:
        print("%d is composite"%(num))
def main():
    num = int(input("enter a number: "))
    prime(num)
main()
