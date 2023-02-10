# Program to concatenate dictionaries

# Sample dictionaries
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

# Concatenate dictionaries
new_dic = {}
for dic in [dic1, dic2, dic3]:
    new_dic.update(dic)

# Print the concatenated dictionary
print(new_dic)