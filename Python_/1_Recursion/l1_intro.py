
def print_n_time(n):
    if n <= 0:
        return
    print_n_time(n-1)
    print(n)    

def sum_of_first_n(n,value=0):
    if n <= 0:
        return value
    return sum_of_first_n(n-1,n+value)

def fact_of_number(n):
    if n==1:
        return 1
    return n * fact_of_number(n-1)

# 1,1,2,3,5,8
def fibonacci(n):
    if n ==1 or n==2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(
   fibonacci(6)
)

