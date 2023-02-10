# Program to generate lowercased version of strings with length greater than 5 using list comprehension

# Sample list of strings
strings = ["HELLO", "WORLD", "PYTHON", "PROGRAMMING"]

# List comprehension to generate lowercased version of strings with length greater than 5
lowercased_strings = [s.lower() for s in strings if len(s) > 5]

# Print the result
print(lowercased_strings)
