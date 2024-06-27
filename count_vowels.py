# Step 1: Define the function that takes a string as an argument
def count_vowels(input_string):
    """
    This function takes a string and returns the count of vowels in the string.
    """
    # Step 2: Initialize a counter for vowels
    vowels_count = 0
    
    # Step 3: Define a set of vowels for quick lookup
    vowels = set("aeiouAEIOU")
    
    # Step 4: Iterate through the string using a for loop
    for char in input_string:
        # Step 5: Check if the current character is a vowel
        if char in vowels:
            vowels_count += 1
    
    # Step 6: Return the count of vowels
    return vowels_count

# Example usage:
example_string = "PowerShell detected that you might be using a screen reader and has disabled PSReadLine for co"
result = count_vowels(example_string)
print(f"The number of vowels in the string is: {result}")