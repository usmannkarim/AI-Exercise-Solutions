#let say  known password is abc$123
known_password = "abc$123"

# taking input from user
username = input("Enter your username: ")
password = input("Enter your password: ")

# compare password to known password using loops
if password.lower() == known_password.lower():
    print("Welcome!")
else:
    print("I don't know you.")
