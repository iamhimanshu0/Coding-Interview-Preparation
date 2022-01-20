"""
# https://leetcode.com/problems/interval-list-intersections/

You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

Input: firstList = [[1,3],[5,9]], secondList = []
Output: []
"""

firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]

def intervalIntersection(firstList, secondList):
    result = []
    Aprt, Bprt = 0, 0 
    
    while Aprt < len(firstList) and Bprt < len(secondList):
        if secondList[Bprt][0] <= firstList[Aprt][1] and firstList[Aprt][0] <= secondList[Bprt][1]:
            result.append(
                [
                    [
                        max(firstList[Aprt][0], secondList[Bprt][0]),
                        min(firstList[Aprt][1], secondList[Bprt][1])
                    ]
                ]
            )

        if firstList[Aprt][1] > secondList[Bprt][1]:
            Bprt +=1
        else:
            Aprt +=1

    return result       

    
    
    
print(
    intervalIntersection(firstList, secondList)
)