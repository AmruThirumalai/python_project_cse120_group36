


def reciprocal(x):
    """
    Computes the reciprocal of a given number x.

    Parameters:
    - x (float): The input number.

    Returns:
    - float: The reciprocal of x.
    """
    if x == 0:
        raise ValueError("Cannot compute reciprocal for x=0")
    return 1 / x

# Example usage:
x_value = 5
result = reciprocal(x_value)
print(f"The reciprocal of {x_value} is: {result}")


#This is the start of the x^2 function code
def square_function(x):
    return x ** 2

# Example usage:
x_value = 36
result = square_function(x_value)
print(f"The square of {x_value} is: {result}")








