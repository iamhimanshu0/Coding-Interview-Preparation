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

print(
    subsetSum([3,1,2])
)