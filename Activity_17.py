def getdata():
    string = input("Enter the string: ")
    return string
def compute(string):
    return [tuple(i.split('=')) for i in string.split(';')]
def display(lst1):
    print(lst1)
def main():
    string = getdata()
    lst1 = compute(string)
    display(lst1)
main()

