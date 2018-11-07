def Permute(arr, i):
	n = len(arr)
	if (i == n-1) : 
		print("Final print : ", arr)
		return

	for j in range(i, n):
		arr[i], arr[j] = arr[j], arr[i]
		Permute(arr, i+1)
		arr[i], arr[j] = arr[j], arr[i]


arr = 'bcef'
i= 0
arr = list(arr)
Permute(arr, i)
