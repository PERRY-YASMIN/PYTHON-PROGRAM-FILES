print("URK24CS1044 SHAIK YASMIN")

# Input a list of elements (can be numbers or strings)
lst = input("Enter elements of the list separated by space: ").split()

# Remove duplicates by converting the list to a set and back to a list
unique_lst = list(set(lst))

# Print the list after removing duplicates
print("List after removing duplicates:", unique_lst)
