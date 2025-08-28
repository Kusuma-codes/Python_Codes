# Program to convert string to datetime
from datetime import datetime

date_string = "2025-08-25 20:15:00"
date_time = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")

print("Datetime:", date_time)
