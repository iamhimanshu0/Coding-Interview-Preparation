"""
Give and list of N intergers, print sums of all subsets in it. Output should be prinited in increasing order of sums

arr  = [2,3]
output = 0, 2, 3, 5

when no elements is taken sum = 0
when only 2 is taken then sum = 2
when only 3 is taken  then sum = 3
when element 2 and 3 are taken then sum = 2+3 = 5
"""

def subsetSum(values):
    output = []
    def find(idx,arr, s):
        if idx == len(values):            
            output.append(s)
            return
              
        arr.append(values[idx])
        find(idx+1, arr, s + values[idx])
        arr.pop()

        find(idx+1, arr, s)
        

    find(0,[],0)
    return sorted(output)

def subset_two(candidates):
    output = []
    candidates.sort()

    def find(idx,arr):
        if idx == len(candidates):
            output.append(arr[:])
            return
        
        for i in range(idx,len(candidates)):
            if i > idx and candidates[i] == candidates[i-1]: continue           

            arr.append(candidates[i])
            find(i+1, arr)
            arr.pop()

    find(0,[])
    return output

"""
    Time Complexity: O(2^N)
    Space Complexity: O(2^N)

    where ‘N’ is the number of elements in ‘ARR’.    
"""

def subSettwo(nums):
    output =  []
    nums.sort()

    def find(nums, idx, arr=[]):
        output.append(arr[:])
        for i in range(idx, len(nums)):
            if i != idx and nums[i] == nums[i-1]:
                continue
            arr.append(nums[i])
            find(nums, i+1, arr)
            arr.pop()

    find(nums, 0,[])
    return output

def subsetsWithDup(nums):
    result=[]
    nums.sort()#To handle duplicate first we sort the array ( adjacent elements will be similar )
    def backtrack(nums,index=0,arr=[]):
        result.append( arr.copy() )
        for i in range( index, len(nums)):
            if i != index and nums[i] ==nums[i-1]: #skip the duplicates, except for the first time
                continue
            arr.append(nums[i]) #include the element
            backtrack(nums,i+1,arr ) #explore
            arr.pop() #remove the element
        
    backtrack(nums)
    return result

print(
    subsetsWithDup([1,1,3]),
    subSettwo([1,1,3])
)