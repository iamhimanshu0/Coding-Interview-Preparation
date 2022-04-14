"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Input: piles = [3,6,7,11], h = 8
Output: 4

Input: piles = [30,11,23,4,20], h = 5
Output: 30

Input: piles = [30,11,23,4,20], h = 6
Output: 23
"""
import math


piles = [30,11,23,4,20]
h = 5

def minEatingSpeedBruteForce(piles, h):
    speed = 1

    while True:
        hour_spent = 0

        for pile in piles:
            hour_spent += math.ceil(pile/speed)

        if hour_spent <= h:
            return speed
        else:
            speed +=1

print(
    minEatingSpeedBruteForce(piles, h)
)


# [3,6,7,11] , h = 8 
"""
eat = 5

current time = 3/5 = 1 ; total time = 0 + 1 = 1
current time = 6/5 = 2 ; total time = 1 + 2 = 3
current time = 7/5 = 2 ; total time = 3 + 2 = 5
current time = 11/5 = 3; total time = 5 + 3 = 8
"""
