# Step Define a function that takes a list of intigers as an argument.
def maximum_number(numbers):
    # Step 2. Initialize a variable for store Maximum number and give it first element of list for now.
    maximum_number = numbers[0]
    # Step 3. Itirate through the list elements with for loop.
    for number in numbers:
        # Step 4. Check if number is greater then maximum_number replace maximum_number Value with it.
        if number > maximum_number:
            maximum_number = number
            # Step 5. Return the maximum_number 
    return maximum_number 

# Usage
sample_input = [10,20,30,40,34,76,89,77,109,58]
result = maximum_number(sample_input)
print(f"The maximum number in the list is: {result}")