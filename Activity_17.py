def inputt():
    string = input()
    return(string)
def convert(string):
    lst = string.split(';')
    tuple1 = tuple(lst)
    lst1 = list(tuple1)
    lst3 = []
    for i in lst1:
        lst2 = i.split('=')
        tuple2 = tuple(lst2)
        lst3.append(tuple2)
    return(lst3)
def output(lst3):
    print(lst3)
def main():
    string = inputt()
    lst3= convert(string)
    output(lst3)
main()
