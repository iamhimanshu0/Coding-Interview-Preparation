"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

https://www.geeksforgeeks.org/count-ways-reach-nth-stair/
"""
n = 3

def fib(n):
    if n <=1:
        return n
    return fib(n-1) + fib(n-2)

def climb_stairs(n):
    return fib(n+1)
    
   

print(climb_stairs(n))