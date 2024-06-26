# Step 1. Define a function which takes a list of integers as an argument.
def count_positive_negative(numbers):
    """
    This Function takes an list of number as an argument and return tuple with count of positive and negetive numbers.
    """

    # Step 2. Initialize counters for positive and negetive numers.
    positive_count = 0
    negative_count = 0
    # Step 3 itrate throug the list with for loop.
    for number in numbers:
        # Step 4 check if the current number is positive.
        if number > 0:
            positive_count += 1 
        # Step 4 check if the current number is positive.
        elif number < 0:
            negative_count += 1

        # Step 6. Return a tuple with the count of positive and negetive numbers.
        return positive_count, negative_count
    
    # Example usage:
example_list = [-1, 2, -3, 4, -5, 6]
result = count_positive_negative(example_list)
print(result)