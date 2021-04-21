#Insertion sort

def InsertionSort(arr):
	for i in range(1,len(arr),1):
		j=i-1
		num = arr[i]
		while(j>=0 and num < arr[j]):
			arr[j+1]=arr[j]
			j=j-1 
		arr[j+1]=num	        
	print(arr)


arr = [12, 11, 2, 13, 5, 6]
InsertionSort(arr)	
