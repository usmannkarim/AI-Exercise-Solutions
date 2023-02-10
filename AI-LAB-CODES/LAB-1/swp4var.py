# Program to swap values of 4 variables using a temporary variable

# Input values for the 4 variables
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
c = int(input("Enter value for c: "))
d = int(input("Enter value for d: "))

# Store the value of a in a temporary variable
temp = a

# Swap the value of a with d
a = d

# Swap the value of d with the value stored in the temporary variable
d = temp

# Store the value of b in a temporary variable
temp = b

# Swap the value of b with c
b = c

# Swap the value of c with the value stored in the temporary variable
c = temp

# Print the values of the 4 variables after the swap
print("Values of a, b, c, and d after swap: ", a, b, c, d)