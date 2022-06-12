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

def rec(st :int,cur :List[int],arr :List[int],subsets:List[List[int]]):

    subsets.append(cur[:])

    for i in range(st,len(arr)):
        
        if i==st or arr[i] != arr[i-1]:

            cur.append(arr[i])
            rec(i+1,cur,arr,subsets)
            cur.pop()

def uniqueSubsets(n :int,arr :List[int]) -> List[List[int]]:
    
    subsets = []
    arr = sorted(arr)
    cur = []
    rec(0,cur,arr,subsets)

    return subsets


print(
    subset_two([1,1,3])
)