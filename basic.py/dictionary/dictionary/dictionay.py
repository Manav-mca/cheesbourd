# Create a dictionary 
my_dict = {"name": "manav", "age": 20, "city": "delhi"}
print(my_dict)

# # Access a values 
# print(my_dict["name"]) 


# # add a new key-value pair
# my_dict["country"] = "india"
# print(my_dict)

# my_dict["subject"] = "science"
# print(my_dict)

# # update a value 
# my_dict["age"] = 21
# print(my_dict)

# # remove a key-value pair 
# del my_dict["city"]
# # print(my_dict)

# # check if a key exists
# if "name" in my_dict:
#     print("key exists")
# else: 
#     print("key does not exist")

# ## get all keys 
# print(my_dict.keys())

# print(my_dict.values())

# # get all items 
# print(my_dict.items())

# loop through a dictionary
for key, value in my_dict.items():
    print(key, value)

# # # clear the dictionary
# my_dict.clear()
# print(my_dict)

## copy a dictionary 

my_dict2 = my_dict.copy()
print(my_dict2)







    