def findZeroSum(arr):
    # Write your code here.
    res = []
    arr.sort()
    for i in range(len(arr) - 2):
        if i >0 and arr[i] == arr[i-1]:
            continue
        l = i + 1
        r = len(arr) - 1
        while l < r:
            sum_ = arr[i] + arr[l] + arr[r]
            if sum_ < 0 :
                l += 1
            elif sum_ > 0:
                r -= 1
            else:
                res.append(str(arr[i]) + " " + str(arr[l]) + " " + str(arr[r]))
                while l < r and arr[l] == arr[l+1]:
                    l += 1
                while l < r and arr[r] == arr[r-1]:
                    r -= 1
                l += 1 ; r -= 1
    return res


arr = [10, 3, -4, 1, -6, 9]
print(findZeroSum(arr))