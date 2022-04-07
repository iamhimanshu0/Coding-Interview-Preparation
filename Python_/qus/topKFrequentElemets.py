"""
Given an integer array nums and an integer k, 
return the k most frequent elements. You may return the answer in any order.

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Input: nums = [1], k = 1
Output: [1]
"""

nums = [3,0,1,0]
k = 1

def topKFrequentElemet(nums, k):
    count = {}

    for i in range(len(nums)):
        if nums[i] not in count:
            count[nums[i]] = 1
        else:
            count[nums[i]] +=1  
    count = {k:v for k, v in sorted(count.items(), key=lambda item: item[1], reverse=True)}
   
    ans = []
    for key, _ in count.items():
        ans.append(key)

    return ans[:k]
        

print(
    topKFrequentElemet(nums,1)
)