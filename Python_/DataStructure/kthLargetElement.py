"""
# https://leetcode.com/problems/kth-largest-element-in-an-array/

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
"""

# O(nlgn) time
import heapq
import random


def findKthLargest1(nums, k):
    return sorted(nums, reverse=True)[k-1]
    
# O(nk) time, bubble sort idea, TLE
def findKthLargest2(nums, k):
    for i in range(k):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                # exchange elements, time consuming
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums[len(nums)-k]
    
# O(nk) time, selection sort idea
def findKthLargest3(nums, k):
    for i in range(len(nums), len(nums)-k, -1):
        tmp = 0
        for j in range(i):
            if nums[j] > nums[tmp]:
                tmp = j
        nums[tmp], nums[i-1] = nums[i-1], nums[tmp]
    return nums[len(nums)-k]
    
# O(k+(n-k)lgk) time, min-heap
def findKthLargest4(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
    for _ in range(len(nums)-k):
        heapq.heappop(heap)
    return heapq.heappop(heap)
    
def findKthLargest(nums, k):
    heap = nums[:k]
    heapq.heapify(heap)
    for n in nums[k:]:
        heapq.heappush(heap, n)
    return heap[0]

# O(k+(n-k)lgk) time, min-heap        
def findKthLargest5(nums, k):
    return heapq.nlargest(k, nums)[-1]
    
# O(n) time, quick selection
def findKthLargest(nums, k):
    # convert the kth largest to smallest
    return findKthSmallest(nums, len(nums)+1-k)
    
def findKthSmallest(self, nums, k):
    if nums:
        pos = self.partition(nums, 0, len(nums)-1)
        if k > pos+1:
            return self.findKthSmallest(nums[pos+1:], k-pos-1)
        elif k < pos+1:
            return self.findKthSmallest(nums[:pos], k)
        else:
            return nums[pos]
 
# choose the right-most element as pivot   
def partition(self, nums, l, r):
    low = l
    while l < r:
        if nums[l] < nums[r]:
            nums[l], nums[low] = nums[low], nums[l]
            low += 1
        l += 1
    nums[low], nums[r] = nums[r], nums[low]
    return low

"""
If you see this problem in competition, the best way just to sort data and choose k-th largest element in O(n log n) overall complexity. However you can imagine, that it is not the good idea for real interview, where your expected do do something else. There is two classical ways how to find order statistic in linear time (yes, it has its mathematical name):

Median of median approach with worst time complexity O(n), however it is quite painful to code and I do not think anyone expect that you do it.
So-called Quick Select, which use similar idea to Quick Sort, with average complexity O(n).
We are going to discuss Quick Select, because it is easier to code:

First, we need to choose so-called pivot and partition element of nums into 3 parts: elements, smaller than pivot, equal to pivot and bigger than pivot. (sometimes two groups enough: less and more or equal)
Next step is to see how many elements we have in each group: if k <= L, where L is size of left, than we can be sure that we need to look into the left part. If k > L + M, where M is size of mid group, than we can be sure, that we need to look into the right part. Finally, if none of these two condition holds, we need to look in the mid part, but because all elements there are equal, we can immedietly return mid[0].
Complexity: time complexity is O(n) in average, because on each time we reduce searching range approximately 2 times. This is not strict proof, for more details you can do some googling. Space complexity is O(n) as well.


"""
nums = [3,2,3,1,2,4,5,5,6]; k = 4
print("start", nums)
def quickSortImplement(nums,k):
    if not nums: return
    
    pivot = random.choice(nums)
    print("Pivot", pivot)
    left = [x for x in nums if x > pivot]
    mid = [x for x in nums if x == pivot]
    right = [x for x in nums if x < pivot]

    print(left, mid, right)
    L, M = len(left), len(mid)
    print("Length" , L,M)

    print(f"k -> {k} L -> {L} M -> {M}")
    if k <= L:
        return quickSortImplement(left,k)
    elif k >L+M:
        return quickSortImplement(right, k-L-M)
    else:
        return mid[0]


print(quickSortImplement(nums, k))