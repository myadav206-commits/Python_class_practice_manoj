import os
import pymysql
import json
from.

def db_connect():
        conn=pymysql.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USEER"),
            password=os.getenv("DB_PASSWORD"),
            port=int(os.getenv("DB_PORT"))
        )
    
        return conn


def db_creation():
        conn=db_connect()
        cur=conn.cursor()
        with open(f"database/schema.json","r") as f:
            data=json.load(f)
            try:
                cur.execute(F"CREATE DATABASE {data["database"]}")
                print(f"Databae {data["database"]} created")
                conn.commit()
            except Exception as e:
                print("Error:",e)
db_connect()


# db_creation()
table=data['tables']
cols="".join([f"str {col} {dcol} for col,dcol in data ['colums'].item()])
print(cols)

def create_table():
      conn=db_connect()
      cur=conn.cursor()
      cur=conn.cursor()
      cur.execute(f"USE" {data['database']})
      cur.execute(f"CREATE TABLE IF NOT EXISTS {TABLE} ({cols}),")

create_table()