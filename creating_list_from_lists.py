def create_new_list(list1, list2):
    # Use list comprehension to create a new list
    result_list = [num for num in list1 if num % 2 != 0] + [num for num in list2 if num % 2 == 0]
    return result_list
# Given lists
# Create a new list based on the conditions
# Print the result
