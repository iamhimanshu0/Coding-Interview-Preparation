# How to find the sum of digits of a positive integer number using recursion?

# Step 1 : Recursive Case - the flow

# 10    10/10 = 1 and Remainder = 0
# 54    54/10 = 5 and Remainder = 4

# 112   112/10 = 11 and Remainder = 2
# 11    11/10 = 1 and Remainder = 1

# idea = f(n) = n%10 + f(n/10)

# Step 2 : Base case - the stopping criterion

# Step 3 : Unintentional case - the constraint


def sumOfDigites(n):
    assert n >= 0 and int(n) == n, "Enter Positive Number Please!"
    if n == 0:
        return 0
    else:
        return int(n % 10) + sumOfDigites(int(n/10))


print(sumOfDigites(23))
