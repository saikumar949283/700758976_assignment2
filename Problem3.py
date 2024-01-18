# Using List Comprehensions
heights_inches = []

# Input heights in inches
print("Enter heights in inches. Type 'done' when finished.")
while True:
    user_input = input("Enter height in inches (or 'done' to finish): ")
    if user_input.lower() == 'done':
        break
    try:
        height_inch = float(user_input)
        heights_inches.append(height_inch)
    except ValueError:
        print("Invalid input. Please enter a valid number or 'done'.")

# Convert heights to centimeters using list comprehensions
heights_centimeters = [round(height * 2.54, 2) for height in heights_inches]

# Print the results
print("Heights in Inches:", heights_inches)
print("Heights in Centimeters:", heights_centimeters)
