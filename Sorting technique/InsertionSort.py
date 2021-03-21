def insertion_sort(a):
    for i in range(1, len(a)):
        temp=a[i]
        j=i-1
        while j>=0 and a[j]>temp:
            a[j+1]=a[j]
            j=j-1
        a[j+1]=temp

list2=[1000, 190, 12, 100, 1920, 920]
insertion_sort(list2)
print(list2)




