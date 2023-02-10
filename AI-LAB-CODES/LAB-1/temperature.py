# Program to convert temperatures to and from Celsius and Fahrenheit

# Function to convert temperature from Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Function to convert temperature from Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Get user input
temp = float(input("Enter temperature: "))
scale = input("Enter scale (Celsius or Fahrenheit): ").lower()

# Check the scale and perform the appropriate conversion
if scale == "celsius":
    temp_in_fahrenheit = celsius_to_fahrenheit(temp)
    print(f"{temp}°C = {temp_in_fahrenheit}°F")
elif scale == "fahrenheit":
    temp_in_celsius = fahrenheit_to_celsius(temp)
    print(f"{temp}°F = {temp_in_celsius}°C")
else:
    print("Invalid scale")