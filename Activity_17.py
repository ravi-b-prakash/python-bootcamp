def getdata():
    return input("Enter the string: ")
def string_to_list_of_tuples(string):
    return [tuple(i.split('=')) for i in string.split(';')]
def display(lst1):
    print(lst1)
def main():
    string = getdata()
    lst1 = string_to_list_of_tuples(string)
    display(lst1)
main()

    
