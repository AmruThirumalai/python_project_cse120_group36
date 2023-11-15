if __name__ == "__main__":
  print("Hello World")


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
