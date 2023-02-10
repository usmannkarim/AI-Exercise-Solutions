# Exercise: List Comprehensions
# Write a list comprehension which, from a list, generates a lowercased version of each string that has length greater than five.

Explanation of the code:

1. Define a sample list of strings strings.

2. Use a list comprehension to iterate over the strings list and generate a lowercased version of each string that has length greater than 5.

3. The expression inside the list comprehension is s.lower() where s is each string from the strings list. The condition to only include strings with length greater than 5 is given by if len(s) > 5.

4. Finally, print the result, which is a list of lowercased strings with length greater than 5.