# sort an array 

def down_heapify(arr,i,n):
	
	parentIndex = i
	leftChildIndex = 2*i+1
	rightChildIndex = 2*i+2
	
	while leftChildIndex < n:
	
		minIndex = parentIndex
		if arr[minIndex] > arr[leftChildIndex]:
			minIndex = leftChildIndex
		if rightChildIndex < n and arr[minIndex] > arr[rightChildIndex]:
			minIndex = rightChildIndex
		
		if minIndex == parentIndex:
			return

		arr[minIndex],arr[parentIndex] = arr[parentIndex],arr[minIndex]
		parentIndex = minIndex
		leftChildIndex = 2*parentIndex+1
		rightChildIndex = 2*parentIndex+2
	return

def heapSort(arr):

	n = len(arr)
	# building head - working on none leaf nodes
	for i in range(n//2,-1,-1):
		down_heapify(arr,i,n)
	
	for i in range(n-1,0,-1):
		arr[0],arr[i] = arr[i],arr[0]
		down_heapify(arr,0,i)
	return 

	# removing min and swapping


arr = [int(ele) for ele in input().split()]
heapSort(arr)

for ele in arr[::-1]:
	print(ele,end=" ")
