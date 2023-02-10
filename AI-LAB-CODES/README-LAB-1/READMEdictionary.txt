# Exercise: Dictionaries
# Write a Python script to concatenate following dictionaries to create a new one.
Sample Dictionary:
	dic1={1:10, 2:20}
	dic2={3:30, 4:40}
	dic3={5:50,6:60}
	Expected Result: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}.


Explanation of the code:

1. Define the sample dictionaries dic1, dic2, and dic3.

2. Create an empty dictionary new_dic to store the concatenated dictionaries.

3. Use a for loop to iterate over a list of the sample dictionaries and use the update method to add the key-value pairs from each dictionary to the new_dic dictionary.

4. Finally, print the concatenated dictionary.