def divide_watermelon(w):
    """
    Determine if a watermelon can be divided into two parts,
    each weighing an even number of kilos for Pete and Billy.

    Parameters:
    - w (int): The weight of the watermelon bought by Pete and Billy.
               Constraints: 1 < w ≤ 100.

    Returns:
    - str: "YES" if the watermelon can be divided into two parts
           with even weights for both Pete and Billy, "NO" otherwise.
    """

    # Check if the weight is greater than 2 and even
    if w > 2 and w % 2 == 0:
        return "YES"
    else:
        return "NO"

# Example usage:
# Read input
w = int(input().strip())

# Call the function with the input and print the result
result = divide_watermelon(w)
print(result)
