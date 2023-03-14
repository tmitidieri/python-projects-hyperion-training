# Different ways to loop over. While use references. For loop reassign. While needs counter and end point. 
# For goes through the list and uses the number of items to iterate.

# -- # Example 1 # -- #
# original_string = input("Please, insert a sentence: ")

# original_list = original_string.split(" ")

# item = 0
# while item < len(original_list):
#     print(original_list[index])
#     index += 1


# -- # Example 2 # -- #
# goo = 0

# other_array= [1,2,4]
# for goo in other_array:
#     print(goo)


# -- # Example 3 # -- #
other_array= ["banana","uva","pera"]
# # for item in other_array:
# #     print(other_array[index])
# #     index += 1

# new_alternated_string = ''
# index = 0
# for item in other_array:
#     if index % 2 == 0:
#         new_alternated_string = new_alternated_string + item.lower() + " "
#     else:
#         new_alternated_string = new_alternated_string + item.upper() + " "
#     index += 1

# print(new_alternated_string)

# -- # Example 4 # -- #
# for index, item in enumerate(other_array):
#     if index % 2 == 0:
#         new_alt_char_string = new_alt_char_string + item.lower()
#     else:
#         new_alt_char_string = new_alt_char_string + item.upper()

# print(new_alt_char_string)


# -- # Verbose example of reversing range # -- #
# num_til_20 = range(0,21)

# index = 0
# for i in num_til_20:
#     index += 1
#     print(num_til_20[-index])


# # # -- # Economic example of reversing range # -- #
# for i in reversed(range(20 + 1)):
#     print(i)

# -- # To manipulate print breaks using end # -- #
# for i in reversed(range(20 + 1)):
#     print(i, end = " ")

# -- # Function that return a result and functions with side effect # -- #
char_list = ['P', 'y', 't', 'h', 'o', 'n']
print(f"Item removed {char_list.pop()}")
# print(char_list.pop())
print(char_list)

char_list.pop(0)
print(char_list)

char_list.remove('t')
print(char_list)