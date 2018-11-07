def mergeArrays(output):
    #
    # Write your code here.
    #
    def merge(arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m
        
        L = [0] * (n1)
        R = [0] * (n2)
        
        for i in range(0,n1):
            L[i] = arr[l + i]
        for j in range(0,n2):
            R[j] = arr[m + 1 + j]
            
        i = 0
        j = 0
        k = l
        
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                k += 1
                i += 1
            else:
                arr[k] = R[j]
                k += 1
                j += 1
        
        while i < n1:
            arr[k] = L[i]
            i+=1
            k+=1
        
        while j < n2:
            arr[k] = R[j]
            j+=1
            k+=1
    
    def mergeSort(arr, l, r):
    	if l < r:
        	print("len(arr) : ", len(arr))
        	m = (l+r)//2
        	print("m : ", m)
        	mergeSort(arr, l, m)
        	mergeSort(arr, m+1, r)
        	merge(arr, l, m, r)
    
    arr = []
    for i in range(len(output)):
        for j in range(len(output[i])):
            arr.append(output[i][j])
    print("output : ", arr)
    low = 0
    high = len(arr) - 1
    mergeSort(arr, low, high)
    return arr


           
output = [[1, 3, 5, 7],
		[2, 4, 6, 8],
		[0, 9, 10, 11]]         
print(mergeArrays(output))






















