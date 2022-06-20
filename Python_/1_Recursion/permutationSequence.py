"""
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

1 "123"
2 "132"
3 "213"
4 "231"
5 "312"
6 "321"

Given n and k, return the kth permutation sequence.

"""

# def getPermutation(n,k):
#     number = [i for i in range(1,n+1)]
#     return number

# print(
#     getPermutation(3,3)
# )

# cascading
def sub1(nums):
    output = [[]]

    for num in nums:
        output += [curr + [num] for curr in output]

    return output    


def subset(nums):
    output = []

    def backtrack(idx, arr, nums):
        if idx == len(nums):
            output.append(arr[:])   
            return

        arr.append(nums[idx])
        backtrack(idx+1, arr, nums)
        arr.pop()

        backtrack(idx+1, arr, nums)
    
    backtrack(0, [], nums)
    return output

def subSettwo(nums):
    output = []

    def backtrack(idx, arr):
        if idx == len(nums):
            output.append(arr[:])
            return
        
        for i in range(idx, len(nums)):
            arr.append(nums[i])
            backtrack(i+1, arr)
            arr.pop()

    for i in range(len(nums)+1):
        backtrack(i,[])
    return output
        
def permuatation(nums):
    output = []
    
    def backtrack(idx, hashmap,arr):
        if idx == len(nums):
            output.append(arr[:])
            return
        
        for i in range(idx, len(nums)):
            if nums[i] not in hashmap:
                arr.append(nums[i])
                hashmap[i] = True
                backtrack(idx+1, hashmap, arr)
                arr.pop()
                hashmap[i] = False
        
    freq = [False]*len(nums)
    backtrack(0, freq, [])
    return output


print(
    # subSettwo([1,2,3])
    permuatation([1,2,3])
)