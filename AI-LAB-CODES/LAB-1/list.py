def count_strings(lst):
    # Initialize a count variable to keep track of the number of strings that match the condition
    count = 0
    # Loop through each string in the list
    for string in lst:
        # Check if the length of the string is 2 or more and the first and last characters are the same
        if len(string) >= 2 and string[0] == string[-1]:
            # If the conditions are met, increment the count
            count += 1
    # Return the final count
    return count

# Sample list of strings
sample_list = ['abc', 'xyz', 'aba', '1221']

# Call the function and store the result in a variable
result = count_strings(sample_list)

# Print the result
print("Number of strings where the string length is 2 or more and the first and last character are the same:", result)
