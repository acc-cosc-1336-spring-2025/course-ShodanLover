# main.py

# Import the decisions module
from decisions import get_options_ratio, get_faculty_rating

# Prompt the user for options
options = float(input("Enter the number of options: "))

# Prompt the user for total
total = float(input("Enter the total number: "))

# Get the options ratio using the get_options_ratio function
result = get_options_ratio(options, total)

# Display the faculty rating based on the ratio
print("Faculty Rating: ", get_faculty_rating(result))
