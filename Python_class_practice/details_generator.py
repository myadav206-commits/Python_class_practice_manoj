import os
import random
import string
ID="".join([random.choice(string.digits+string.ascii_uppercase) for i in range(9)])
meeting_id="".join([random.choice(string.digits+string.ascii_uppercase) for i in range(16)])
def create_details(files):
    for i in files:
        if ".txt" in i:
            print(f"files : {i}")
    select=input("select your file without ext :")
    with open(f"{select}.txt", "w") as file:
        file.write(f"name : {select}"+"\n")
        file.write(f"Candidate_Id : {ID}"+"\n")
        file.write(f"meeting_id : https://{meeting_id}"+"\n")
        file.write(f"Candidate_email : {input("enter your email : ")}"+"\n")
    print(f"{select} file updated...")
files=os.listdir()
create_details(files)
