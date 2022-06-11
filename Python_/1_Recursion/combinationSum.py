"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Input: candidates = [2], target = 1
Output: []
"""

def combinationSum(candidates, target):
    # return candidates
    output = []
    def find(idx, arr):
        if idx == len(candidates):
            if sum(arr) == target and sorted(arr) not in output:
                output.append(sorted(arr[:]))
            return
    
        arr.append(candidates[idx])
        find(idx+1, arr)
        arr.pop()

        find(idx+1, arr)

    find(0, [])
    return output

def combinationSum2(candidates, target):
    output = []

    def find(idx,target, ds):
        if idx == len(candidates):
            if target == 0:                
                output.append(sorted(ds[:]))
            return 

        if candidates[idx] <= target:
            ds.append(candidates[idx])
            find(idx, target- candidates[idx], ds)
            ds.pop()

        find(idx+1,target, ds) 

    
    find(0, target, [])

    return output

def combinationSumWorking(candidates, target):
    output = []
    candidates.sort()

    def find(idx, target, output, arr):
        if target == 0:
            output.append(arr[:])
            return
        
        for i in range(idx,len(candidates)):
            if i > idx and candidates[i] == candidates[i-1]: continue
            if candidates[i] > target: break

            arr.append(candidates[i])
            find(i+1,target-candidates[i], output, arr)
            arr.pop()

    find(0, target, output, [])
    return output



print(
    # combinationSumWorking([2,3,4,6],7),
    combinationSumWorking([10,1,2,7,6,1,5],8)
)