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
    start = int(input("Enter start number: "))
    stop = int(input("Enter stop number: "))
    loop(start, stop)
main()
