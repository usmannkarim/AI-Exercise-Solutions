# Exercise: Lists
# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
Sample List : ['abc', 'xyz', 'aba', '1221'] Expected Result : 2.

Explanation:
The count_strings function takes a list of strings as its argument. Inside the function, we have an integer variable count that is initialized to zero and will be used to keep track of the number of strings that match the condition.

The function loops through each string in the list using a for loop. For each string, the function checks if the length of the string is 2 or more and the first and last characters are the same. If both conditions are met, the value of count is incremented by 1.

Finally, the function returns the final value of count which is the number of strings that match the condition.

In the main program, we have a sample list of strings sample_list and we call the count_strings function, passing the sample list as an argument. The result of the function is stored in a variable result and printed to the console.