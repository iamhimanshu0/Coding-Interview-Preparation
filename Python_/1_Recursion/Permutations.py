"""
You are given a string ‘str’ consisting of lowercase letters. Your task is to return all permutations in string in any order.

Sample Input
abc
Sample Output 
abc acb bac bca cab cba
"""

# TC :- n! * n  :- n! beacuse need to find all the permutations and n is for looping though

# SC :- o(n) + o(n) :- o(n) is for sotring the hashmap and o(n) is for storing the arr 
def printInt(s):
    output =[]

    def find(idx, hashmap, arr):
        if idx == len(s):
            output.append(arr[:])
            return

        for i in range(idx, len(s)):
            if s[i] not in hashmap:
                arr.append(s[i])
                hashmap[i] = True
                find(idx+1, hashmap, arr)
                hashmap[i] = False
                arr.pop()
    
    freq = [False]*len(s)
    find(0, freq, [])
    return output

# TC :- n! * n  :- n! beacuse need to find all the permutations and n is for looping though

# SC :- O(n)
def printInt2(s):
    # output = []

    def find(idx, arr):
        if idx == len(s):
            print(arr)
        else:
            for i in range(idx, len(s)):
                s[idx], s[i] = s[i], s[idx]
                # arr.append(s[i])
                find(idx+1, arr)
                s[idx], s[i] = s[i], s[idx]
                # arr.pop()
    
    find(0,[])
    # return output

def permuteString(s):
    
    def find(a, l, r):
        if l == r:
            print("".join(a))
        else:
            for i in range(l,r):
                a[l], a[i] = a[i], a[l]
                find(a, l+1, r)
                a[l], a[i] = a[i], a[l]

    find(s,0, len(s))




    
print(
#     printString(["a","b","c"])
    printInt([1,2,3]),
# permuteString(list("ABC"))
)