"""Write a program that generates and prints a multiplication table for a given number.
Use a for loop to iterate through numbers 1 to 10 (or any range you choose)."""

# start with multiple of 2s
# write the formula for multiple of 2s
# list it out in a loop.
# Do it 3 times

nums = int(input("Enter the number you would you like to use for multiples (e.g., 5s, 2s, 4s). "))

multiples = int(input("Enter how many times you want to multiply. "))

for i in range(multiples):
    multiply = nums * (i + 1)
    print(multiply)