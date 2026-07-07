# import pymysql
# import json
# # STEP 1 : FILE FETCH
# with open("table.json") as f:
#     schema=json.load(f)
# # STEP 2 : DB CONNECTION
# pymy_sql_db=pymysql.connect(
#                             host="localhost",
#                             user="root",
#                             password="root"
#                             )
# db_name=schema['database']

# mysql_db=pymy_sql_db.cursor()
# # STEP 3 : DB CONNECTION AND USE 
# mysql_db.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
# print(f'"DATABASE": {db_name} IS READY TO USE')
      
# mysql_db.execute(f"use {db_name}")

# col_defination=[f"for {col} {dtype}" for col,dtype in schema["colums"].items() ]
# print(col_defination)

# mysql_db.execute(f"create table if exists {schema["table_name"]} ({col_defination})")
# print("table created using json schema")

# # step 4 
# row_defination=student_schema["students"]
# print(row_defination)

# mysql_db.commit()
# curser.close()
# mysql_db.close()  