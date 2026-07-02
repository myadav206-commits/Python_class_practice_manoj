import json
with open ("product.json","r") as file:
    python_data=json.load(file)
    # print(type(python_data))
with open("clean_json.txt","w") as text_file:
    for key,value in python_data.items():
        text_file.write(f"{key},{value}")
    # print(python_data["id"])
    # print(python_data["title"])
    # print(python_data["description"])
# folder_name = "output_folder"
# os.makedirs(folder_name, exist_ok=True)
# with open("product.json", "r") as file:
#     python_data = json.load(file)
# file_path = os.path.join(folder_name, "clean_json.txt")
# with open(file_path, "w") as file:
#     file.write(f"ID: {python_data['id']}\n")
#     file.write(f"Title: {python_data['title']}\n")
#     file.write(f"Description: {python_data['description']}\n")
# print("clean_json.txt file created")



