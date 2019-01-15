from sys import argv
# read the WYSS section fro how to run this
script, first, second, third = argv

print("The script is called:" , script)
print("Your first variable is:" , first)
print("Your second variable is:" , second)
print("Your third variable is:" , third)

variable = input("What would you like your next varriable to be? ")
print(f"Your last varriable is: {variable} ")
