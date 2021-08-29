def input_numbers():
    a=int(input())
    b=int(input())
    return a, b
def add(a, b):
    addition = a+b
    return addition
def display(a, b, summation):
    print("%d + %d = %d"%(a,b,summation))
def main():
    a, b = input_numbers()
    summation = add(a, b)
    display(a, b, summation)
main()
