# How to calculate power of a number using recursion?

# Step 1 : Recursive Case - the flow
# x^n = n * x^n-1

# Step 2 : Base case - the stopping criterion

# Step 3 : Unintentional case - the constraint


def powerOfNumber(number, power):
    assert power >= 0 and int(power) == power  "Please add only positive number for Power"
    if power == 0:
        return 1
    if power == 1:
        return number
    else:
        return number * powerOfNumber(number, power-1)

print(powerOfNumber(3,1))