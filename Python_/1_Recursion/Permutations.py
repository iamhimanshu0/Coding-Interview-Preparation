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

 
def printInt2(s):
    pass

def printString(s):
    output = []

    def find(idx,arr):
        if idx == len(s):
            output.append(arr[:])
            return
        
        for i in range(idx, len(s)):
            arr.append(s[i])
            find(i+1, arr)
            arr.pop()
        


    find(0,[])
    return output
    
print(
    # printString("abc")
    printInt([1,2,3])
)