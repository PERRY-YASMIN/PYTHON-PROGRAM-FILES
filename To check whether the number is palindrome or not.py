print("URK24CS1044 SHAIK YASMIN")
number = int(input("Enter the number: ")) temp = number
reverse =0

while (number > 0): 
  digit = number % 10
  reverse = reverse * 10 + digit number = number // 10
  print("The reverse number is: ", reverse) if temp==reverse:
  print("The number is a palindrome") else:
  print("The number is not a palindrome")
