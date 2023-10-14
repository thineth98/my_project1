# Function to convert meters to kilometers
def meters_to_kilometers(meters):
    kilometers = meters / 1000  # 1 kilometer = 1000 meters
    return kilometers

# Input from the user
meters = float(input("Enter the length in meters: "))

# Convert meters to kilometers
kilometers = meters_to_kilometers(meters)

# Display the result
print(f"{meters} meters is equal to {kilometers} kilometers")
