# Define a lambda function that takes a string and a character as inputs and returns a boolean value
starts_with = lambda string, char: string[0] == char

# Prompt the user to enter a string and a character
string = input("Enter a string: ")
char = input("Enter a character: ")

# Call the lambda function to check if the string starts with the given character
if starts_with(string, char):
    print("The string starts with the character ", char)
else:
    print("The string does not start with the character ", char)
