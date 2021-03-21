def bubblesort(a):
    swap=0
    for i in range(len(a)-1):

        for j in range(len(a)-i-1):
            if a[j]>a[j+1]:
                a[j], a[j+1]=a[j+1], a[j]
                swap+=1
        if swap==0:
            break
    print("Swap value", swap)
list1=[22,11,34,21]
bubblesort(list1)



for i in range(0,len(list1)):
    print(list1[i])


