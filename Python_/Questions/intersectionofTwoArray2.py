"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.

"""

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

def intersect(nums1, nums2):
    intersectArray = []
    
    # build hasmap
    check = {}
    for n in range(len(nums1)):
        if nums1[n] in check:
            check[nums1[n]] +=1
        else:
            check[nums1[n]] =1    
    

    for n in range(len(nums2)):
        if nums2[n] in check:
            if check[nums2[n]] > 0:
                intersectArray.append(nums2[n])
                check[nums2[n]] -=1
        else:
            pass

    return intersectArray

def intersect2Pointer(nums1, nums2):
    nums1.sort()
    nums2.sort()
    output = []
    i,j = 0,0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i+=1
        elif nums1[i] > nums2[j]:
            j+=1
        else:
            output.append(nums1[i])
            i+=1
            j+=1
    return output



print(
    intersect2Pointer(nums1, nums2)
)