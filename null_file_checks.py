import os
import time
from datetime import datetime, timedelta

# Set the NAS directory path
nas_path = r"C:\Users\locha\Downloads"  # Replace with your NAS directory path

# Get the current time and calculate the required time range
current_time = datetime.now()
yesterday_6pm = datetime(current_time.year, current_time.month, current_time.day, 18, 0) - timedelta(days=1)
today_5pm = datetime(current_time.year, current_time.month, current_time.day, 17, 0)

# Convert the times to timestamps (seconds since epoch)
yesterday_6pm_timestamp = time.mktime(yesterday_6pm.timetuple())
today_5pm_timestamp = time.mktime(today_5pm.timetuple())

# Function to check files and print those within the time range
def check_null_files_in_time_range(nas_path):
    # List to store files within the time range
    null_files = []

    # Walk through the directory
    for root, dirs, files in os.walk(nas_path):
        for file in files:
            # Check if the file is a .null file (or any other criteria you want)
            if file.lower().endswith('.null'):
                file_path = os.path.join(root, file)
                
                # Get the last modified time of the file
                file_mtime = os.path.getmtime(file_path)
                
                # Check if the file was modified within the time range
                if yesterday_6pm_timestamp <= file_mtime <= today_5pm_timestamp:
                    null_files.append(file_path)

    # Return the list of files found
    return null_files

# Get the null files modified in the given time range
null_files = check_null_files_in_time_range(nas_path)

# Print the results
if null_files:
    print("The following null files list 6 PM and today 5 PM:")
    for file in null_files:
        print(file)
else:
    print("No null files were found in the specified time range.")
