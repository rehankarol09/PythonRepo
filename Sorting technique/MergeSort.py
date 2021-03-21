def merge(a):
    if len(a)>1:
        mid=len(a)//2

        A=a[:mid]

        B=a[mid:]

        merge(A)

        merge(B)

        i=0
        j=0
        k=0

        while i<len(A) and j<len(B):
            if A[i]<=B[j]:
                a[k] = A[i]
                i += 1
            else:
                a[k]=B[j]
                j+=1
            k+=1

        while i<len(A):
            a[k]=A[i]
            i+=1
            k+=1

        while j<len(B):
            a[k]=B[j]
            j+=1
            k+=1

if __name__ == '__main__':
    list1 = [6, 3, 1, 5, 9]
    merge(list1)
    print(list1, end=" ")


