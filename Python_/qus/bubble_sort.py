
"""
bubble sort is also refreed as sinking sort
we repeatedly compare each pair of adjacent items and swap them
if needed
"""

def bubble(list):
    for i in range(len(list)):
        for j in range(len(list)):
            if list[i] < list[j]:
                list[i], list[j] = list[j], list[i]

    return list 


a = [5,3,1,2,8,4,7,6,9]

print(bubble(a))

"""
    # time complexity = O(N^2)
    # space complexity = O(1)

    # when to use
        #  - when the input is already sorted
        #  - space is a concern
        #  - Easy to implment


    # when to avoid
        # - Average time complexity is poor
"""