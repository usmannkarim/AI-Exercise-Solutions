# Program to print a specified list after removing specified elements

# Sample list
colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow', 'Teapink']

# Remove specified elements
new_colors = [color for i, color in enumerate(colors) if i not in [0, 4, 5]]

# Print the result
print(new_colors)
