""" 
    in case of selection sort we repeatedly find the minimun element and 
    move it to the sorted part of array to make unsorted part sorted.
"""

def selection(list):
    for i in range(len(list)):
        min_value = i 
        for j in range(i+1,len(list)):
            if list[min_value] > list[j]:
                min_value = j

        list[i], list[min_value] = list[min_value], list[i]

    return list

a = [5,3,1,2,8,4,7,6,9]

print(selection(a))


"""
    # time complexity = O(N^2)
    # space complexity = O(1)

    # when to use
        #  - when we have insufficient memory
        #  - Easy to implment


    # when to avoid
        # - when time is a concern
"""