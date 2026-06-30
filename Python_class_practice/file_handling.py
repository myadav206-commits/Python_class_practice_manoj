#_________________file handling_________________
# 1. file handling in python means reading from and writing to files/folder stored on disk using python.
# 2. your python code can open a file pull out data of it , put data into it and also close it properly.


# what is file

# files are store  of data and information on the specific path of device

# types of files
# 1. text file(.txt,.csv,.json)
# 2 binary file( image,video,audio)


# types of file path
# 1. absolute : the complete path from the root of the filesystem
# #2. relative path : the path reletive to where your current folder(current working dir)

#  file mode
# 1. a : append , a+ : append and read
# 2. w : write , w+ : write and read
# 3. r : read , r+ : read and write
# 4. x : strictly create file
 
#  python file handling method.
# 1. open(file_name,mode) : opens file
# 2. close () : close file.
# 3. flush() : memoey cleanup
# 4. read() : file read
# 5. readlines (): file read line by line.
# 6. write () : writes data in file only take string
# 7. write data in file of any data types
# 8. tail(): cursor move
# 9. seek(): specific position set of cursor
 
# 1. create a file in strict mode
# try:
#     file=open("strict.txt","x")
#     print("file created..")
# except.exception as e:
#     print("error : file can not created")

# file=open("write.txt","w")
# file.write("this is completely python file handling")
# file.flush()
# file.close()
# print("file created..")

# context manager
# with open ("manager.txt","w+") as file:
#     file.write("this is completely python file handling..")
#     file.seek(5)
#     r=file.read(4)
#     print("file created and written")
#     print(f"file content : {r}")

# with open("demo.txt","r") as f:
#     r=f.read()
#     if r.isdigit():
#         print(r)

# emp_list=["aman","shivam","shubham","anshu","kamal","dev"]
# # emp name individual file create txt type.
# for i in emp_list:
#     emp_list = i + ".txt"
#     with open(emp_list, "w") as file:
#         file.write(i)
# print("All employee text files created successfully.")
   
# import os
# print(os.listdir())
# print("current folder :",os.getcwd())
# path=r"c:Amit Yadav\Desktop\Python_Class_Practice_Manoj\Python_class_practice"
# os.chidr(path)
# print("current folder",)
# # with open("os.txt","w") as file
# emp_list=["aman","shivam","shubham","anshu","kamal","dev"]
# for i in emp_list:
#     file_check=os.path.exists(f"{i}.txt")
#     if not file_check:
#      with open(f"{i}.txt","w") as file:
#         print((f"{i}.txt file created..."))
# else:
#     print(f"{i} - file already exists")
# folder="employee_details"
# os.makedirs(folder)
# emp_list=["aman","shivam","shubham","anshu","kamal","dev"]
# for i in emp_list:
#    os.remove(f"{i}".txt)
#    print(i,"removed..")
# target=os.getcwd()+folder
# path=os.chdir(target)
# print(path)