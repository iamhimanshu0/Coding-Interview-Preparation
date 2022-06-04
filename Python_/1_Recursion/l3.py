

# print all subsequences  [which follows the orders]
"""
    [3,1,2]
=   [], [3],[1],[2],[3,1],[1,2],[3,2]

(power set)

# we can't take [2,3] or [1,3] because they are not following order
"""

"""
arr = [3,2,1]
idx = [0,1,2]
    code structure

    f(ind, [])
    {
        n = len([])
        # base case 
        if(ind >= n){
            print([])
            return;
        }

        [].add(arr[i])  --> case of take
        f(ind+1, [])
        [].remove(arr[i]) -- > case of not take
        f(ind+1, [])

    }

    main(){
        arr = [3,2,1]
        f(0,[])
    }

"""
def print_sequence(idx,val, array,n):
    if idx == n:
        for i in val:
            print(i, end=" ")
        print("")
        return
    
    # take the element 
    val.append(array[idx])
    print_sequence(idx+1, val, array, n)
    val.pop()

    # not take
    print_sequence(idx+1, val, array, n)

def print_all_subsequences(array):
    n = len(array)
    val = []
    print_sequence(0, val, array, n)


print(
    print_all_subsequences([3,1,2])
)

# TC :-> o(2^n * n)
# Sc :-> 0(n)  ;- n length of array