"""
# hackerrank.com/challenges/mini-max-sum/problem?isFullScreen=true
"""

arr = [1,3,5,7,9]

def minMaxSum(arr):
    arr.sort()
    minSum = sum(arr[:-1])
    maxSum = sum(arr[1:])

    print(minSum, maxSum)

print(
    minMaxSum(arr)
)
