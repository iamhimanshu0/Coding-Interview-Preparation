# reverse an array

# using 2 pointer
def rev(l,r, arr):
    if l>=r: return
    arr[l],arr[r] = arr[r], arr[l]
    rev(l+1, r-1, arr)

# using only 1 pointer
def rev1(i,arr):
    """
        n = len(arr) ==  5
        n-1-1 == (5-1-1) = 4(get forth index)
        n-2-1 == (5-2-1) = 3(get third index)

        until i>n//2 (or in middle)
    """
    n = len(arr)
    if i>n//2:
        return
    arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    rev1(i+1, arr)

def reverse_array(arr):
    # rev(0,len(arr)-1, arr)
    rev1(0, arr)
    return arr



# -------------------------
def check(idx, value):
    n = len(value)

    if idx > n//2:
        return True
    
    if value[idx] != value[n- idx -1]:
        return False
    
    return check(idx+1, value)

def pallindrome(value):
    return(check(0, value))

# print(reverse_array([3,1,4,2,5]))
print(pallindrome("hima"))
print(pallindrome("raccar"))