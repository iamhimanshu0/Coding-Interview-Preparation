# How to covert a number from Decimal to Binary using Recursion

# Step 1 : Recursive Case - the flow
    # - Divide the number by 2
    # - Get the integer quotient for the next iteration
    # - Get the remainder for the binary digit
    # - Repeat the steps  until the quotient is equal to 0

    # f(n) =  remainder + 10 * (divided/2)
    # f(n) = n mod 2 + 10 * (f/2)
 

# Step 2 : Base case - the stopping criterion
    # -if n == 0 (quotient == 0)

# Step 3 : Unintentional case - the constraint


def decimalToBinary(n):
    assert int(n) == n , "Please Enter Positive Value!"
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * decimalToBinary(int(n/2))
     


print(decimalToBinary(10))