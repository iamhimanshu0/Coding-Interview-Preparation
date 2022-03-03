"""
# https://leetcode.com/problems/find-the-town-judge/

In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

- The town judge trusts nobody.
- Everybody (except for the town judge) trusts the town judge.
- There is exactly one person that satisfies properties 1 and 2.

You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

Input: n = 2, trust = [[1,2]]
Output: 2

Input: n = 3, trust = [[1,3],[2,3]]
Output: 3

Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
"""

"""
Reframing the question :-
There are 1 to n people in a town with one of them being a judge. The criteria to being a judge is that :-

1. The judge believes no one than himself.
2. Whole town i.e Everybody believes judge .

So at the end of the statement the constraints leads to pointing out that any person that is trusted by N-1 persons and the same person believes no one, then the preson is said to be a judge.

Intuition:-
A basic intuition can be concluded from question is that, if a person is believing someone else than himself than that person is not qualified for being a judge or if a person is trusted by others and has everyone's favour i.e total of N-1 favours, than this person is truly the judge.

Algorithm:-

Create an array Trusted of size N+1 to represent the total number of peoples in a town and initialize it with 0 .
After initialization, whenever a person trust someone else than himself, the trusted value of that person should be decreased since that person is not satisfying the two conditions that were mentioned in the question.
Also if a certain x person is trusted by others from town, than this x person value should be increased and those who trusted that x person there values should be decreased.
At last traverse through every person of town and while traversing If a person is found with N-1 trusts than this person should be the judge and return the index of that person .

"""

n = 3
trust = trust = [[1,3],[2,3],[3,1]]

def findJudge(n, trust):
    Trusted = [0]*(n+1)
    for (a,b) in trust:
        print(a,b)
        Trusted[a] -=1
        Trusted[b] +=1

        # print(Trusted)

    for i in range(1, len(Trusted)):
        if Trusted[i] == n-1:
            return i
    return -1



print(
    findJudge(n, trust)
)