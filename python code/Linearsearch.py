def linearsearch(a, n, search_value):
    for i in range(n):
        if a[i] == search_value:
            return i
    return -1
if __name__ == '__main__':
    n=int(input("Enter the no of element you want in array"));
    a=[None]*n
    for i in range(n):
        a[i]=int(input("enter elements"))

    x=linearsearch(a, n, 11)
    if x == -1:
        print("Element not found")
    else:
        print("Element found at ", x, " position")



