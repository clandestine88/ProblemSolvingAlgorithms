def solve(arr):
	dic = {}
	for elem in arr:
		temp = elem.split()
		if temp[0] in dic:
			dic[temp[0]].append(temp[1])
		else:
			dic[temp[0]] = [temp[1]]
	
	print("dic: ",dic)
 
arr = ["key1 abcd", "key2 zzz", "key1 hello", "key3 world", "key1 hello"]
solve(arr)