def inputt():
    start = int(input("Enter start number: "))
    stop = int(input("Enter stop number: "))
    return(start, stop)
def loop(start, stop):
    for i in range(start, stop):
        if (i%2==0):
            continue
        else:
            if (i!=stop-1 and i!=stop-2):
                print(i,end=', ')
            else:
                print(i)
def main():
    start, stop = inputt()
    loop(start, stop)
main()
