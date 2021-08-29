def inputt():
    string = input("Enter string list: ")
    strlist = string.split()
    return strlist
def sorts(strlist):
    strlist1 = sorted(strlist)
    print("USING SORTED()")
    print("sorted list: ",end = " ")
    print(strlist1)
    print("original list: ",end = " ")
    print(strlist)
    print()
    strlist.sort()
    print("USING SORT()")
    print("sorted list: ",end = " ")
    print(strlist)
    print("original list: ",end = " ")
    print(strlist)
def main():
    strlist = inputt()
    sorts(strlist)
main()
