# Write a program that checks if a specific element exists in a given tuple and prints an appropriate message.

print("** Check if an Element Exists in a Tuple **")

# Define a tuple
my_tuple = (1, 2, 3, 4, 5)

# Input the element to search for
element = int(input("Enter an element to check: "))

# Check if the element exists in the tuple
if element in my_tuple:
    print(f"{element} exists in the tuple.")
else:
    print(f"{element} does not exist in the tuple.")


# GitHub : jaleedkhanofficial
# linkedin.com/in/jaleedkhanofficial