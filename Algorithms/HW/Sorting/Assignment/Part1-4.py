def topK(arr, k):
    def heapifyMax(arr, n, i):
        left = 2 * i + 1
        right = 2 * i +2 
        largest = i
        
        if left < n and arr[left] > arr[largest]:
            largest = left
            
        if right < n and arr[right]> arr[largest]:
            largest = right
            
        if largest != i :
            arr[i], arr[largest] = arr[largest], arr[i]
            heapifyMax(arr, n, largest)
        
        
    def buildMaxHeap(arr, n):
        for i in range(n//2 - 1, -1, -1):
            heapifyMax(arr, n , i)
    

    def getKthLargestElement(arr, k):
        i = len(arr) - 1
        j = 0
        while i >=0 and j<k :
            arr[i], arr[0] = arr[0], arr[i]
            heapify(arr, i, 0)
            i -= 1
            j += 1
        return arr[len(arr) - k]
    
    def heapExtractMax(arr, n):
        temp = arr[0]
        arr[0] = arr[n-1]
        n = n-1
        heapifyMax(arr, n, 0)
        return temp
        
    def printLargestK(arr, n , k):
        buildMaxHeap(arr, n)
        res = []
        check = {}
        i= 0
        while i < k:
            max_element = heapExtractMax(arr, n)
            if max_element in check:
                k += 1
            else:
                check[max_element] = 1
                res.append(max_element)
            i+=1
        return res
    
    
    n = len(arr)
    return printLargestK(arr, n, k)


arr = [1, 5, 5, 4, 4, 2, 1, 14, 18, 17, 17]
k = 5

print(topK(arr, k))

