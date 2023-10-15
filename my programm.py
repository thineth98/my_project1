# Get the length in centimeters from the user
centimeters = float(input("Enter a length in centimeters: "))

# Convert centimeters to meters
meters = centimeters / 100

# Display the result
print(f"{centimeters} centimeters is equal to {meters} meters")


#new progarame for this
# Function to convert feet to centimeters
def feet_to_centimeters(feet):
    centimeters = feet * 30.48  # 1 foot = 30.48 centimeters
    return centimeters

# Input from the user
feet = float(input("Enter the length in feet: "))

# Convert feet to centimeters
centimeters = feet_to_centimeters(feet)

# Display the result
print(f"{feet} feet is equal to {centimeters} centimeters")
