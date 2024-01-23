def create_new_list(list1, list2):
    # Use list comprehension to create a new list
    result_list = [num for num in list1 if num % 2 != 0] + [num for num in list2 if num % 2 == 0]
    return result_list

# Given lists
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

# Create a new list based on the conditions
result_list = create_new_list(list1, list1)

# Print the result
print("Result list:", result_list)