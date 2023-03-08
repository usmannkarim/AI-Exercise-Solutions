# Define a lambda function that takes a datetime string as input and returns a tuple of year, month, date, and time.
get_date_time = lambda dt_string: (dt_string[:4], dt_string[5:7], dt_string[8:10], dt_string[11:19])

# Prompt the user to enter a datetime string..
dt_string = input("Enter a datetime string (yyyy-mm-dd hh:mm:ss): ")

# Call the lambda function to extract the year, month, date, and time.
year, month, date, time = get_date_time(dt_string)

# Print the extracted values...
print("Year:", year)
print("Month:", month)
print("Date:", date)
print("Time:", time)
