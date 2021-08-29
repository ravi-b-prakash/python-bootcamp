def inputt():
    string = input()
    return(string)
def convert(string):
    lst = string.split(';')
    return(lst)
def output(lst):
    print([tuple(i.split('=')) for i in lst])
def main():
    string = inputt()
    lst = convert(string)
    output(lst)
main()

