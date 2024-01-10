def div_by_three():
    """ Returns if a number is divisble by three """

    x = int(input("Enter a number "))           # Enter your number
    quota = x/3
    print(x, "divided by three equals ", quota) # Prints number, and quota
    return quota.is_integer()                   # If the quota is an integer returns True, else False

is_integer = div_by_three()                     # Assigns is integer to the function
print(is_integer)                               # Prints True or False


def max2(x, y):
    """ Returns the greatest value of two numbers"""
    
    if x > y:           # If x is greater, return y
        return x
    else:               # Else return y
        return y
    
def max3(x, y, z):
    """ Returns greatest value of three numbers """

    max_2 = max2(x, y)      # Calls max2 with x, y and returns the greater value
    return max2(max_2, z)   # returns the greater value of previous value and z

result = max3(2, 5, 4)
print(result)