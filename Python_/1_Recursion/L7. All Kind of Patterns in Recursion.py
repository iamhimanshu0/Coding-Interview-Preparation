"""
Given an array arr[] of length N and a number K, the task is to find all the subsequences of the array whose sum of elements is K

Examples:  

Input: arr[] = {1, 2, 3}, K = 3 
Output: 
1 2 
3

Input: arr[] = {17, 18, 6, 11, 2, 4}, K = 6  
Output: 
2 4 
6  

"""
# printing subsequences whose sum is k
def sum_is_k(nums, k):
    output = []
    def find(idx, arr):
        if idx == len(nums):
            if sum(arr) == k:
                output.append(arr[:])
            return 

        arr.append(nums[idx])
        find(idx+1, arr)
        arr.pop()

        find(idx+1, arr)

    find(0, [])
    return output

# printing subsequences whose sum is k (only one answer)
def sum_is_k_one(nums, k):
    output = []
    def find(idx, arr):
        if idx == len(nums):
            # condition is satisfied
            if sum(arr) == k:
                output.append(arr[:])
                return True
                
            # condition is not satisfied
            return False

        arr.append(nums[idx])

        if(find(idx+1, arr) == True):
            return True      

        arr.pop()

        if(find(idx+1, arr) == True):
            return True

        return False

    find(0, [])
    return output

print(
    sum_is_k_one([17, 18, 6, 11, 2, 4],6),
    sum_is_k_one([1,2,3,4],6)
)