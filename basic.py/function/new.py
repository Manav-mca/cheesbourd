# # # # # # li = [1,2,3,4,5]
# # # # # # li.pop(2)
# # # # # # print(li)
# # # # # # li.append(6)
# # # # # # print(li)
# # # # # # li.insert(2,10)
# # # # # # print(li)
# # # # # # li.remove(10)
# # # # # # print(li)
# # # # # # li.remove(4)
# # # # # # print(li)
# # # # # # li.reverse()
# # # # # # print(li)
# # # # # # li.sort()
# # # # # # print(li)
# # # # # # li.clear()
# # # # # # print(li)
# # # # # # li = [1,2,"Hello","sir", 3]
# # # # # # li.pop(2)
# # # # # # print(li)

# # # # # l1 = [1,2,3,4]
# # # # # l2 = [5,6,7,8,9]
# # # # # k = l1+l2
# # # # # print(k)
# # # # # # 

# # # # l1 = [1,2,3,4]
# # # # l1.insert(3,"python ")
# # # # l1.append("list")
# # # # print(l1)


# # # tuple1 = (1,2,3,4,5)
# # # value = int(input("Enter a value to check if it is persent in the tuple :"))

# # # if value in tuple1:

# # #     print(f"{value} is present in the tuple.")
# # # else:
# # #     print(f"{value} is not persent in the tuple.")
    

    
# # d1 = {1: "one", 2: "two", 3: "three", 4: "Manav", 5: "five"}
# # print(d1.keys())
# # print(d1.values())
# # print(d1.items())
# # print(d1.get(4))


# # create a dictionary
# d1= {1: "rahul", 2: "manav", 3: "sahil", 4: "sachin", 5: "priyanshu"}

# # access a value using a key
# print(d1[3])

# ## add a new key-value pair
# d1[6] = "lala ji"
# print(d1)

# # update an existing key-value pair
# d1[1] = "rahul kumar"
# print(d1)

# # delete a key-value pair 
# del d1[6]
# print(d1)

# # check if a key exists in the dictionaty 
# name = int(input("Enter a key to check if it exists in the dictionary : "))

# if name in d1:
#     print("key", {name},"exists in the dictionary :", d1[2])
# else:
#     print("key ",{name},"does not exist in the dictionary :", d1)



d1 = {1: "rahul", 2: "manav", 3: "sahil", 4: "sachin", 5: "priyanshu"}

# # print the keys of the dictionary 
# print("Keys of the dictionary: ", d1.keys())

# #print the valrues of the dictionary 
# print("Values of the dictionary: ", d1.values())

# print("Items of the dictionaary: ", d1.items())

# # get the value of a key
# input_key = int(input("Enter a key to get its value :"))

# print("Value of key :", {input_key} ,":", d1.get(input_key))


# #Loop through a dictionary
# for keys, values in d1.items():
#     print(f"key: {keys}, value: {values}")

# # add a new key-value pair
# d1[6] = "lala ji"
# print("After adding a new key-value pair : ", d1)
# # update ane existing key-value pair
# d1[1] = "rahul kumar"
# print("After updating an existing key-value pair : ", d1)


#copy a dictionary
d1 = d1.copy()
print("After copying the dictionary : ", d1)
