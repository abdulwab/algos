# Step 1. Define the function that takes a list of integers as an argument.
def sum_of_odd_numbers(numbers):
    """
    This function takes a list of integers and returns the sum of all odd numbers in the list.
    """
    # Step 2. Initialize a variable to store the sum of odd numbers.
    sum_odd = 0

    # Step 3. Iterate through the list using a for loop
    for number in numbers:
        # Step 4. Check if the current number is odd using the modulus operater.
        if number % 2 != 0:
            # Step 5. If the number is odd, add it to the sum_odd variable.
            sum_odd += number

    # Step 6. Return the sum of odd numbers after the loop has finished
    return sum_odd

# usage 

numbers_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
result = sum_of_odd_numbers(numbers_list)
print(result)