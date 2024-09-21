from datetime import date

# Function to calculate age
def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year
    
    # Adjust the age if the birthday hasn't occurred yet this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    
    return age

# Input: Get birth date from user
year = int(input("Enter your birth year: "))
month = int(input("Enter your birth month: "))
day = int(input("Enter your birth day: "))

# Create a date object for the birth date
birth_date = date(year, month, day)

# Calculate age
age = calculate_age(birth_date)

# Output the result
print(f"You are {age} years old.")
