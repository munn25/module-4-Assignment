#problem 1-current date and time
from datetime import datetime
# Get current date and time
current_datetime = datetime.now()

# Display current date and time
print("Current Date and Time:", current_datetime.strftime("%Y-%m-d %H:%M:%S"))