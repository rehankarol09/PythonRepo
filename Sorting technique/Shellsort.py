def shellsort(a):
    h=int(input("Enter increment value"))
    while h>=1:
        for i in range(h,len(a)):
            temp=a[i]
            j=i-h
            while j>=0 and a[j]>temp:
                a[j+h]=a[j]
                j=j-h
                print(j)

            a[j+h]=temp
        h=h-2
list1=[23, 12, 31, 78]
shellsort(list1)
print(list1)