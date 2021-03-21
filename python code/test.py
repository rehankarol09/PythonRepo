def mergeSort(a): 

    if len(a) >1: 

        mid = len(a)//2

        A = a[:mid]

        B = a[mid:]

        mergeSort(A) 

        mergeSort(B) 

        i = j = k = 0    

        while i <len(A) and j <len(B):

            if A[i] < B[j]: 

                a[k] = A[i] 

                i+=1

            else: 

                a[k] = B[j] 

                j+=1

            k+=1

        while i <len(A):

            a[k] = A[i] 

            i+=1

            k+=1       

        while j <len(A):

            a[k] = B[j] 

            j+=1

            k+=1 


if __name__ == '__main__':

    a = [12, 11, 13, 5, 6, 7]   

    mergeSort(a) 

    print('Sorted array is: ', end='')

    for i in range(len(a)):
        print(a[i],end=" ")