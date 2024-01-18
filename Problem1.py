def fullname(first_name, last_name):
    return first_name + " " + last_name

def string_alternative(full_name):
    return full_name[::2]

# Get user input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Get full name using the fullname function
full_name = fullname(first_name, last_name)

# Get every other character using the string_alternative function
result = string_alternative(full_name)

# Display the result
print(f"Full Name: {full_name}")
print(f"Every other character: {result}")
