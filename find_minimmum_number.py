# Step 1. Define function that takes a list of integers as an argument.
def find_minimum(numbers):
    """
    This function takes list of integers as argument and returns minimmum number in the list.
    """
    # Step 2. Initialize a variable to store minimmum number, starting with the first element of the list.
    mini_number = numbers[0]

    # Step 3. Iterate through the list using for loop.
    for number in numbers:
        # Step 4. Check if the currrent number is less then current minimmum number.
       if mini_number > number:
           # Step 5. Replace the minimmum number with current number if this is less then minimmum number.
           mini_number = number

    # Step 6. Return the minimmum number found in the list.
    return mini_number 

# Example usage:
example_list = [21, 52, 3, 764, 775, 86, 25, 54, 33, 764, 775, 86]
result = find_minimum(example_list)
print(f"The minimum number in the list is: {result}")