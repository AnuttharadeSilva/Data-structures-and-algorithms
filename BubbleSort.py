def BubbleSort(arr):
    for i in range(1,len(arr)):
        for j in range(len(arr)-i):
            if(arr[j]>arr[j+1]):
                x = arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=x
    print(arr)

arr = [64, 34, 25, 12, 22, 11, 90]
BubbleSort(arr)