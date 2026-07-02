Name : .aman
Emp_Id: char+digits
file_name=["aman,txt","anshu.txt","dev.txt","kamal.txt"]
with open 

import json
import os
folder_name = "output_folder"
os.makedirs(folder_name, exist_ok=True)
with open("product.json", "r") as file:
    python_data = json.load(file)
file_path = os.path.join(folder_name, "clean_json.txt")
with open(file_path, "w") as file:
    file.write(f"ID: {python_data['id']}\n")
    file.write(f"Title: {python_data['title']}\n")
    file.write(f"Description: {python_data['description']}\n")

print("clean_json.txt file created")