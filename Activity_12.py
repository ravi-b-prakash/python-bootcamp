def inputt():
    a = int(input())
    b = int(input())
    c = int(input())
    return(a, b, c)
def greatest(a, b, c):
    if (a>=b) and (a>=c):
        return a
    elif (b>=c) and (b>=a):
        return b
    else:
        return c
def output(big, a, b, c):
     print("%d is the greatest number among %d, %d and %d"%(big, a, b, c))
def main():
    a, b, c = inputt()
    big = greatest(a, b, c)
    output(big, a, b, c)
main()
    
    
