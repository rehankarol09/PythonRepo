def reverselist(a,start,end):
    if start>=end:
        return
    a[start],a[end]=a[end],a[start]
    reverselist(a,start+1,end-1)

if __name__ == "__main__":
    a=[11,22,33,44,55]
    print(a)
    reverselist(a,0,4)
    print("After reversing : ")
    print(a)