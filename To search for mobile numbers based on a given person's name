print("URK24CS1044 SHAIK YASMIN")
people = []
for i in range(5):
    name = input(f"Enter name of person {i+1}: ")
    mobile_number = input(f"Enter mobile number of {name}: ")
    people.append((name, mobile_number))  # Store as tuple

search_name = input("Enter the name to search for their mobile number: ")
found = False
for person in people:
    if person[0].lower() == search_name.lower():  # Case-insensitive comparison
        print(f"Mobile number of {search_name}: {person[1]}")
        found = True
        break

if not found:
    print(f"Name '{search_name}' not found in the list.")
