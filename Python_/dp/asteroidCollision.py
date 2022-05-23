"""
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
"""
asteriods = [10,2,-5]

def asteroidCollision(asteriods):
    """
        # We only need to resolve collisions under the following conditions:
        # - stack is non-empty
        # - current asteroid is -ve
        # - top of the stack is +ve
    """
    result = []

    for i in range(len(asteriods)):
        while len(result) > 0 and asteriods[i] < 0 and result[-1] > 0:
            # if both are same destory both
            if result[-1] == -asteriods[i]:
                result.pop()
                break
            # stack top is smaller, remover the +ve astroid from the stack and continue comparison
            elif result[-1] < -asteriods[i]:
                result.pop()
                # continue
            # stack top is larget destory -ve 
            elif result[-1] > - asteriods[i]:
                break

        else:
            # -ve astroid made it all the way to the bottom of the stack and destoryed all asteriods
            result.append(asteriods[i])
        
    return result


print(
    asteroidCollision(asteriods)
)