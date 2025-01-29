print("URK24CS1044 SHAIK YASMIN")

# Input a list of strings (can be taken from user or hardcoded)
strings = input("Enter a list of words separated by space: ").split()

# Convert the list to a set to get unique words
unique_words = set(strings)

# Create a dictionary to store the frequency of each word
word_frequency = {}

# Count the frequency of each unique word
for word in unique_words:
    word_frequency[word] = strings.count(word)

# Print the word frequency
print("Word frequency:")
for word, count in word_frequency.items():
    print(f"{word}: {count}")
