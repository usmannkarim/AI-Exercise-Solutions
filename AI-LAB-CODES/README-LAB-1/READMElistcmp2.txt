# Exercise: List Comprehensions
# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements Sample List: ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow',’Teapink’]
  Expected Output: ['Green', 'White', 'Black’, ‘Teapink’]

Explanation of the code:

1. Define a sample list colors.

2. Use a list comprehension to remove the 0th, 4th, and 5th elements from the colors list. The expression inside the list comprehension is color and the index of each element is given by i. The condition to only include elements whose index is not 0, 4, or 5 is given by if i not in [0, 4, 5].

3. Finally, print the result, which is a list containing elements of the colors list excluding the 0th, 4th, and 5th elements.