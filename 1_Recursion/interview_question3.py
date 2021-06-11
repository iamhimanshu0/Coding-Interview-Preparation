# How to find GCD (Greatest Common Divisor) of two numbers using recursion?

# Step 1 : Recursive Case - the flow
# GCD is the largest positive interger that divides the numbers without a remainder
# gcd(8,12) = 4
  # 8 = 2 * 2 * 2
  # 12 = 2 * 2 * 3

# Euclidean algorithms
#  gcd(48,18)
# step 1 : 48/18 = 2 remainder 12
# step 2 : 18/12 = 1 remainder 6
# step 3 : 12/6 =  2 remainder 0    === (so for gcd (48,18) is 6)
    # gcd (a,0) = a
    # gcd (a,b) = gcd(b, a mod b)


# Step 2 : Base case - the stopping criterion
# b  == 0

# Step 3 : Unintentional case - the constraint
#  - positive integers
#  - covert negative to positive

def GCD(a, b):
    assert int(a)== a and int(b) == b , "Number should be Integer!"
    if a < 0 or b < 0:
        a = -1 * a
        b = -1 * b

    if b == 0:
        return a 
    else:
        return GCD(b, a % b)
    

print(GCD(-48, -18))