def getdata():
    string = input()
    return(string)
def compute(string):
    lst = string.split(';')
    lst1 = [tuple(i.split('=')) for i in lst]
    return(lst1)
def display(lst1):
    print(lst1)
def main():
    string = getdata()
    lst1 = compute(string)
    display(lst1)
main()
