def quicksort(a, low, high):
    if low<high:
        pi = partition(a, low, high)
        quicksort(a, low, pi - 1)
        quicksort(a, pi + 1, high)



def partition(a, low, high):
    pivot=a[high]
    i=low-1
    for j in range(low, high):
        if a[j]<pivot:
            i+=1
            a[i], a[j]=a[j], a[i]
    a[i+1], a[high]=a[high], a[i+1]
    return i+1

list1=[89, 78, 100, 8]
quicksort(list1, 0, len(list1)-1)
print(list1)


