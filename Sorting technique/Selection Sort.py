def selectionsort(a):
    for i in range(len(a)-1):
        minindex=i
        for j in range(i+1, len(a)):
            if a[j]<a[minindex]:
                minindex=j
        if i!=minindex:
            a[i], a[minindex]=a[minindex], a[i]

if __name__ == '__main__':
    list1=[43, 21, 34, 32]
    selectionsort(list1)
    print(list1)
