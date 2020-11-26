import os
import datetime

image_name = input("Please enter directory path:\n")
print(os.listdir(image_name))

time_list = []

file_count = {}

for file_name in os.listdir(image_name):
    file_path = image_name + "\\" + file_name
    file_time = os.path.getmtime(file_path)
    proper_time = datetime.datetime.fromtimestamp(file_time)
    if proper_time not in time_list:
        time_list.append(proper_time)
    else:
        print(f"Deleting file: {file_path}")
        os.remove(file_path)
