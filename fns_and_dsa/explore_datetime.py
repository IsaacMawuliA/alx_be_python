# Import the necessary components from the datetime module
from datetime import datetime

# Function to display the current date and time
def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)

# Call the function to display the current date and time
display_current_datetime()

# Import the necessary components from the datetime module
from datetime import datetime, timedelta

# Function to calculate a future date
def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    current_date = datetime.now()
    future_date = current_date + timedelta(days=number_of_days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print("Future date:", formatted_future_date)

# Call the function to calculate a future date
calculate_future_date()

