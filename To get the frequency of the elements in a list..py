print("URK24CS1044 SHAIK YASMIN")

# Create an empty list
A = []
# Input the size of the list
n = int(input("Enter the size of the List :: "))
print("Enter list elements:")
# Input the elements and append them in the list
for i in range(n):
    k = int(input())  # Take input for each element and append to the list
    A.append(k)
# Create a dictionary to store frequency
frequency = {}
# Count the frequency of each element in the list
for i in A:
    if i in frequency:
        frequency[i] += 1  # Increment count if element is already in dictionary
    else:
        frequency[i] = 1   # Initialize the count if element is not in the dictionary
# Print the frequency of each element
print("Frequency of elements:", frequency)
